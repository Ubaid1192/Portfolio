# 📄 POST Requests

## Overview  
This document contains example POST requests for manual API testing. These cover resource creation, authentication, user interaction, and data submission scenarios. Each example includes method, URL, headers, request body, expected HTTP status, and response payload.

## Table of Contents  
1. [Create New User](#1-create-new-user)  
2. [User Login](#2-user-login)  
3. [Submit Product Review](#3-submit-product-review)  
4. [Upload Image](#4-upload-image)  
5. [Create Order](#5-create-order)


## 1. Create New User  

**Method:** POST  
**URL:** https://api.example.com/users  
**Headers:**  

- Authorization: Bearer `<token>`  
- Content-Type: application/json  
- Accept: application/json  

**Body:**  

```json
{
  "name": "Eve",
  "email": "eve@example.com",
  "password": "securePassword123"
}
```

**Expected Response:**  
**Expected HTTP Status:** 201 Created

```json
{
  "id": 51,
  "name": "Eve",
  "email": "eve@example.com"
}
```

---

## 2. User Login  

**Method:** POST  
**URL:** https://api.example.com/auth/login  
**Headers:**  

- Content-Type: application/json  
- Accept: application/json  

**Body:**  

```json
{
  "email": "eve@example.com",
  "password": "securePassword123"
}
```

**Expected Response:**  
**Expected HTTP Status:** 201 Created  
> *or 200 OK, it depends on implementation*

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 51,
    "name": "Eve",
    "email": "eve@example.com"
  }
}
```

---

## 3. Submit Product Review  

**Method:** POST  
**URL:** https://api.example.com/products/101/reviews  
**Headers:**  

- Authorization: Bearer `<token>`  
- Content-Type: application/json  
- Accept: application/json  

**Body:**  

```json
{
  "rating": 5,
  "comment": "Excellent wireless mouse. Smooth performance and great battery life."
}
```

**Expected Response:**  
**Expected HTTP Status:** 201 Created  

```json
{
  "review_id": 202,
  "product_id": 101,
  "rating": 5,
  "comment": "Excellent wireless mouse. Smooth performance and great battery life.",
  "author": "Eve"
}
```

---

## 4. Upload Image  

**Method:** POST  
**URL:** https://api.example.com/uploads/images  
**Headers:**  

- Authorization: Bearer `<token>`  
- Content-Type: multipart/form-data  
- Accept: application/json  

**Body (form fields):**  

- `file`: binary image file (e.g., `mouse.jpg`)  
- `description`: "High-resolution product image for wireless mouse"  

**Expected Response:**  
**Expected HTTP Status:** 201 Created  

```json
{
  "upload_id": 302,
  "filename": "mouse.jpg",
  "description": "High-resolution product image for wireless mouse",
  "url": "https://cdn.example.com/uploads/mouse.jpg"
}
```

---

## 5. Create Order  

**Method:** POST  
**URL:** https://api.example.com/orders  
**Headers:**  

- Authorization: Bearer `<token>`  
- Content-Type: application/json  
- Accept: application/json  

**Body:**  

```json
{
  "products": [
    { "product_id": 101, "quantity": 2 },
    { "product_id": 106, "quantity": 1 }
  ],
  "shipping_address": {
    "street": "123 Market St",
    "city": "Techville",
    "postal_code": "12345",
    "country": "USA"
  },
  "payment_method": "credit_card"
}
```

**Expected Response:**  
**Expected HTTP Status:** 201 Created  

```json
{
  "order_id": 707,
  "status": "processing",
  "estimated_delivery": "2025-08-04",
  "total": 149.99,
  "products": [
    {
      "product_id": 101,
      "name": "Wireless Mouse",
      "quantity": 2
    },
    {
      "product_id": 106,
      "name": "Wireless Charger",
      "quantity": 1
    }
  ]
}
```
