# 📄 PUT Requests

## Overview  
This document contains example PUT requests used in manual API testing. These are intended for full resource updates, such as changing user details or replacing entire objects. Each example includes method, URL, headers, request body, expected HTTP status, and response.

## Table of Contents  
1. [Update User Profile](#1-update-user-profile)  
2. [Replace Product Details](#2-replace-product-details)

---

## 1. Update User Profile  
**Method:** PUT  
**URL:** https://api.example.com/users/51  
**Headers:**  

- Authorization: Bearer `<token>`  
- Content-Type: application/json  
- Accept: application/json  

**Body:**  
```json
{
  "name": "Eve Cooper",
  "email": "eve.cooper@example.com",
  "phone": "+1-555-1234",
  "address": {
    "street": "456 Innovation Rd",
    "city": "Techville",
    "postal_code": "54321",
    "country": "USA"
  }
}
```

**Expected Response:**  
**Expected HTTP Status:** 200 OK

```json
{
  "id": 51,
  "name": "Eve Cooper",
  "email": "eve.cooper@example.com",
  "phone": "+1-555-1234",
  "address": {
    "street": "456 Innovation Rd",
    "city": "Techville",
    "postal_code": "54321",
    "country": "USA"
  },
  "updated_at": "2025-07-30T17:49:00Z"
}
```

---

## 2. Replace Product Details  
**Method:** PUT  
**URL:** https://api.example.com/products/101  
**Headers:**  

- Authorization: Bearer `<token>`  
- Content-Type: application/json  
- Accept: application/json  

**Body:**

```json
{
  "name": "Wireless Mouse Pro",
  "description": "Ergonomic wireless mouse with customizable DPI and silent buttons.",
  "price": 49.99,
  "stock": 120,
  "category": "Accessories"
}
```

**Expected Response:**  
**Expected HTTP Status:** 200 OK

```json
{
  "product_id": 101,
  "name": "Wireless Mouse Pro",
  "description": "Ergonomic wireless mouse with customizable DPI and silent buttons.",
  "price": 49.99,
  "stock": 120,
  "category": "Accessories",
  "updated_at": "2025-07-30T18:02:00Z"
}
```
