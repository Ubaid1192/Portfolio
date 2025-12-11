# 📄 GET Requests

## Table of Contents
1. [Retrieve All Users](#1-retrieve-all-users)
2. [Retrieve User by ID](#2-retrieve-user-by-id)
3. [Filter Users by Role](#3-filter-users-by-role)
4. [Paginated Products List](#4-paginated-products-list)
5. [Search Products by Keyword](#5-search-products-by-keyword)

## Overview  
This document describes example GET requests used in manual API testing. These cover basic data retrieval, filtering, and pagination scenarios. Each example includes method, URL, headers, and expected response behavior.

---

## 1. Retrieve All Users  
**Method:** GET  
**URL:** https://api.example.com/users  
**Headers:**  
- Authorization: Bearer `<token>`  
- Content-Type: application/json  
- Accept: application/json  

**Expected Response:** 
**Expected HTTP Status:** 200 OK

```json
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  },
  {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com"
  }
]
```

---

## 2. Retrieve User by ID  
**Method:** GET  
**URL:** https://api.example.com/users/42  
**Headers:**  
- Authorization: Bearer `<token>`  
- Accept: application/json  

**Expected Response:**  
**Expected HTTP Status:** 200 OK

```json
{
  "id": 42,
  "name": "Charlie",
  "email": "charlie@example.com"
}
```

**Error Response if not found:**
**Expected HTTP Status:** 404 Not Found

```json
{
  "error": "User not found"
}
```

---

## 3. Filter Users by Role  
**Method:** GET  
**URL:** https://api.example.com/users?role=admin  
**Headers:**  
- Authorization: Bearer `<token>`  
- Accept: application/json  

**Expected Response:**  
**Expected HTTP Status:** 200 OK

```json
[
  {
    "id": 10,
    "name": "Dana",
    "role": "admin"
  }
]
```

---

## 4. Paginated Products List  
**Method:** GET  
**URL:** https://api.example.com/products?page=2&limit=3  
**Headers:**  
- Authorization: Bearer `<token>`  
- Accept: application/json  

**Expected Response:**  
**Expected HTTP Status:** 200 OK

```json
{
  "products": [
    {
      "id": 101,
      "name": "Wireless Mouse"
    },
    {
      "id": 102,
      "name": "USB Keyboard"
    },
    {
      "id": 103,
      "name": "HD Monitor"
    }
  ],
  "pagination": {
    "page": 2,
    "limit": 3,
    "total_items": 9
  }
}
```

---

## 5. Search Products by Keyword  
**Method:** GET  
**URL:** https://api.example.com/products?search=wireless  
**Headers:**  
- Authorization: Bearer `<token>`  
- Accept: application/json  

**Expected Response:**  
**Expected HTTP Status:** 200 OK

```json
[
  {
    "id": 101,
    "name": "Wireless Mouse"
  },
  {
    "id": 106,
    "name": "Wireless Charger"
  }
]
```
