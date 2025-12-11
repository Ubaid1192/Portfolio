from locust import HttpUser, task, between, constant, SequentialTaskSet, events
import random
import string
import logging
import json
import os
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bdd_load_test.log'),
        logging.StreamHandler()
    ]
)

# Test configuration
class TestConfig:
    FAILURE_THRESHOLD = 1  # Maximum allowed failure percentage
    MIN_REQUESTS = 10      # Minimum number of requests to consider test valid
    MAX_RESPONSE_TIME = 2000  # Maximum allowed response time in milliseconds
    REPORT_DIR = "load_test_reports"

class Statistics:
    def __init__(self):
        self.total_requests = 0
        self.failed_requests = 0
        self.max_response_time = 0
        self.start_time = datetime.now()
        
    @property
    def failure_percentage(self):
        if self.total_requests == 0:
            return 0
        return (self.failed_requests / self.total_requests) * 100

class UserBehavior(SequentialTaskSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.registered_users = []
        self.stats = Statistics()
        
    def generate_random_string(self, length=8):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    
    def generate_random_user(self):
        random_string = self.generate_random_string()
        return {
            'fullName': f'Test User {random_string}',
            'userName': f'testuser_{random_string}',
            'email': f'test_{random_string}@example.com',
            'password': f'password_{random_string}',
            'phone': ''.join(random.choices(string.digits, k=10))
        }
    
    def log_scenario(self, scenario, status, details=""):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{timestamp}] Scenario: {scenario} | Status: {status} | Details: {details}"
        logging.info(message)
        
        # Update statistics
        self.stats.total_requests += 1
        if status in ["FAIL", "ERROR"]:
            self.stats.failed_requests += 1
    
    @task
    def scenario_register_new_user(self):
        """
        Feature: User Registration
        Scenario: Register a new user with random data
        Given a new user with random credentials
        When sending a registration request
        Then registration should be successful
        """
        user_data = self.generate_random_user()
        
        with self.client.post("/client_registeration", 
                            data=user_data, 
                            catch_response=True,
                            name="1. Register New User") as response:
            try:
                if response.json()['msg'] == 'User Registered':
                    self.log_scenario("Registration", "SUCCESS", f"User: {user_data['email']}")
                    response.success()
                    self.registered_users.append(user_data)
                else:
                    self.log_scenario("Registration", "FAIL", 
                                    f"User: {user_data['email']}, Error: {response.json()['msg']}")
                    response.failure(response.json()['msg'])
            except Exception as e:
                self.log_scenario("Registration", "ERROR", str(e))
                response.failure(f"Invalid response: {str(e)}")
            
            # Track response time
            self.stats.max_response_time = max(self.stats.max_response_time, response.elapsed.total_seconds() * 1000)

    @task
    def scenario_login_with_email(self):
        """Scenario: Login with email for recently registered user"""
        if not self.registered_users:
            self.log_scenario("Login with Email", "SKIP", "No registered users available")
            return
            
        # Given: A registered user's credentials
        user = random.choice(self.registered_users)
        
        # When: Attempting to login with email
        payload = {
            'userName': '',
            'email': user['email'],
            'password': user['password']
        }
        
        with self.client.post("/client_login", 
                            data=payload, 
                            catch_response=True,
                            name="2. Login with Email") as response:
            try:
                # Then: Login should be successful and return a token
                if 'token' in response.json():
                    self.log_scenario("Login with Email", "SUCCESS", f"User: {user['email']}")
                    response.success()
                else:
                    self.log_scenario("Login with Email", "FAIL", 
                                    f"User: {user['email']}, Error: {response.json().get('msg', 'Unknown error')}")
                    response.failure(response.json().get('msg', 'Login failed'))
            except Exception as e:
                self.log_scenario("Login with Email", "ERROR", str(e))
                response.failure(f"Invalid response: {str(e)}")
    
    @task
    def scenario_login_with_username(self):
        """Scenario: Login with username for recently registered user"""
        if not self.registered_users:
            self.log_scenario("Login with Username", "SKIP", "No registered users available")
            return
            
        # Given: A registered user's credentials
        user = random.choice(self.registered_users)
        
        # When: Attempting to login with username
        payload = {
            'userName': user['userName'],
            'email': '',
            'password': user['password']
        }
        
        with self.client.post("/client_login", 
                            data=payload, 
                            catch_response=True,
                            name="3. Login with Username") as response:
            try:
                # Then: Login should be successful and return a token
                if 'token' in response.json():
                    self.log_scenario("Login with Username", "SUCCESS", f"User: {user['userName']}")
                    response.success()
                else:
                    self.log_scenario("Login with Username", "FAIL", 
                                    f"User: {user['userName']}, Error: {response.json().get('msg', 'Unknown error')}")
                    response.failure(response.json().get('msg', 'Login failed'))
            except Exception as e:
                self.log_scenario("Login with Username", "ERROR", str(e))
                response.failure(f"Invalid response: {str(e)}")

def generate_junit_report(stats):
    """Generate JUnit XML report for CI/CD integration"""
    report_dir = Path(TestConfig.REPORT_DIR)
    report_dir.mkdir(exist_ok=True)
    
    junit_template = f"""<?xml version="1.0" encoding="UTF-8"?>
<testsuites>
    <testsuite name="Load Test Results" tests="{stats.total_requests}" failures="{stats.failed_requests}">
        <testcase name="Performance Requirements" classname="LoadTest">
            {'<failure message="Failed performance requirements"/>'}
        </testcase>
    </testsuite>
</testsuites>"""
    
    with open(report_dir / "load_test_results.xml", "w") as f:
        f.write(junit_template)

@events.quitting.add_listener
def on_test_end(environment, **kwargs):
    """Handle test completion and generate reports"""
    if not environment.stats.total.num_requests:
        logging.error("No requests were made during the test!")
        environment.process_exit_code = 1
        return
    
    # Calculate test results
    failure_percent = (environment.stats.total.num_failures / environment.stats.total.num_requests) * 100
    avg_response_time = environment.stats.total.avg_response_time
    
    # Generate test report
    report = {
        "total_requests": environment.stats.total.num_requests,
        "failed_requests": environment.stats.total.num_failures,
        "failure_percentage": failure_percent,
        "average_response_time": avg_response_time,
        "test_duration": str(datetime.now() - environment.runner.stats.start_time)
    }
    
    # Create report directory
    report_dir = Path(TestConfig.REPORT_DIR)
    report_dir.mkdir(exist_ok=True)
    
    # Save JSON report
    with open(report_dir / "load_test_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    # Generate JUnit report
    generate_junit_report(environment.stats.total)
    
    # Determine test success/failure
    failed = (
        failure_percent > TestConfig.FAILURE_THRESHOLD or
        avg_response_time > TestConfig.MAX_RESPONSE_TIME or
        environment.stats.total.num_requests < TestConfig.MIN_REQUESTS
    )
    
    if failed:
        logging.error("Load test failed to meet requirements!")
        environment.process_exit_code = 1
    else:
        logging.info("Load test completed successfully!")
        environment.process_exit_code = 0

class WebsiteUser(HttpUser):
    wait_time = constant(1)
    fixed_count = 10
    tasks = [UserBehavior] 