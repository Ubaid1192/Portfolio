# 📄 DELETE Requests

## Overview  
This document contains example DELETE requests used in manual API testing. These requests are designed to remove resources such as users, products, and reviews. Each example includes method, URL, headers, expected HTTP status, and the typical structure of a response (if any).

## Table of Contents  
1. [Delete User by ID](#1-delete-user-by-id)  
2. [Delete Product by ID](#2-delete-product-by-id)  
3. [Delete Review by ID](#3-delete-review-by-id)

---

### 1. Delete User by ID

**Method:** DELETE  
**URL:** https://api.example.com/users/{user_id}  
**Headers:**  
  Authorization: Bearer <valid_token>  

**Expected Response:**  
- HTTP Status: 204 No Content  
- Body: Empty (indicating successful deletion)  

**Notes:**  
- Attempting to delete a non-existent user should return 404 Not Found.  
- If token is missing or invalid -> 401 Unauthorized.

---

### 2. Delete Product by ID

**Method:** DELETE  
**URL:** https://api.example.com/products/{product_id}  
**Headers:**  

- Authorization: Bearer <valid_token>  

**Expected Response:**  

- HTTP Status: 200 OK  
- Body:

```json 
  {
    "message": "Product deleted successfully",
    "deleted_product_id": "123456"
  }
```

**Notes:**  
- If the product with the given ID does not exist -> 404 Not Found  
- Missing or invalid token -> 401 Unauthorized  
- Deletion may be blocked if the product is linked to an active order -> 409 Conflict

---

### 3. Delete Review by ID

**Method:** DELETE  
**URL:** https://api.example.com/reviews/{review_id}  
**Headers:**  

- Authorization: Bearer <valid_token>  

**Expected Response:**  
- HTTP Status: 200 OK  
- Body:  

```json
  {
    "message": "Review deleted successfully",
    "deleted_review_id": "r001"
  }
```

**Notes:**  
- If the review does not exist -> 404 Not Found  
- Missing or invalid token -> 401 Unauthorized  
- Deletion may be restricted if the review is under dispute -> 403 Forbidden

---