# 🔌 API Testing

## Overview

This folder contains documentation for manual API testing performed on various endpoints. It includes example requests, testing strategies, and reusable reference notes. All requests and validations are described in Markdown and reflect common practices used in QA portfolios.

---

## 📁 Available Request Files

This folder includes categorized `.md` files with manual API requests organized by HTTP method. Each file contains examples and notes for:

- Authentication and session validation  
- Data creation, retrieval, and deletion  
- Header and payload formatting  
- Common error scenarios and edge cases

List of available request files:

- [GET_Requests.md](GET_Requests.md) - read operations, pagination testing, query parameters  
- [POST_Requests.md](POST_Requests.md) - resource creation, field validation, authentication flow  
- [PUT_Requests.md](PUT_Requests.md) - full object replacement, structure and status checks  
- [DELETE_Requests.md](DELETE_Requests.md) - safe deletion handling, token validation, conflict responses

---

## Example Tools Used

- [Postman](https://www.postman.com/)  
- [Fiddler Web Debugger](https://www.telerik.com/fiddler)  
- [cURL](https://curl.se/)  
- [Swagger / OpenAPI](https://swagger.io/)  
- [VS Code REST Client plugin](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)  
- [Google Chrome built-in DevTools (Network tab)](https://developer.chrome.com/docs/devtools/network/)

---

## Common HTTP Methods Used

These are the most frequently used HTTP methods in REST API testing:

| Method | Purpose                         | Example Usage              |
|--------|----------------------------------|----------------------------|
| **GET**    | Retrieve data                    | Get user list              |
| **POST**   | Create a new resource            | Create a new review        |
| **PUT**    | Fully replace a resource         | Update all user fields     |
| **PATCH**  | Partially update a resource      | Change only email address  |
| **DELETE** | Remove a resource                | Delete a product           |

Other standard HTTP methods include:

| Method   | Description                                      |
|----------|--------------------------------------------------|
| **OPTIONS**  | Returns supported methods for a resource         |
| **HEAD**     | Similar to GET but returns headers only          |
| **TRACE**    | Echoes back the received request (debugging)     |
| **CONNECT**  | Establishes tunnel (used in HTTPS via proxy)     |

---

## Common HTTP Response Codes

Here are the most commonly encountered status codes during testing:

| Code | Meaning                    | Notes                                |
|------|----------------------------|--------------------------------------|
| **200**  | OK                         | Successful response                  |
| **201**  | Created                    | Resource successfully created        |
| **204**  | No Content                 | Successful deletion/update, no body |
| **301**  | Moved Permanently          | Resource moved to a new URL         |
| **302**  | Found                      | Temporary redirect                   |
| **304**  | Not Modified               | Client has cached version            |
| **400**  | Bad Request                | Invalid request data                 |
| **401**  | Unauthorized               | Missing or invalid token             |
| **403**  | Forbidden                  | Action not allowed                   |
| **404**  | Not Found                  | Resource does not exist              |
| **409**  | Conflict                   | Data conflict (e.g. product in use)  |
| **429**  | Too Many Requests          | Rate limit exceeded                  |
| **500**  | Internal Server Error      | Server-side issue                    |
| **502**  | Bad Gateway                | Invalid response from upstream server |
| **503**  | Service Unavailable        | Server temporarily overloaded/unavailable |
| **504**  | Gateway Timeout            | Server didn’t respond in time        |

---
