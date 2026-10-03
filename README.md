# FastAPI A to Z 🚀

A complete **FastAPI A-to-Z learning journey** covering everything from basic API development to authentication, databases, file uploads, email verification, and deployment.

This repository contains practical examples, exercises, and projects built while learning **FastAPI and modern backend development with Python**.

## 📌 Project Overview

The goal of this repository is to build a strong foundation in **FastAPI backend development** by learning concepts step by step and implementing them through practical projects.

The repository starts with basic API concepts and gradually moves toward advanced backend features such as:

* REST APIs
* CRUD operations
* Pydantic
* SQLAlchemy
* Authentication & Authorization
* JWT
* OAuth2
* Password hashing
* Admin authentication
* File and image uploads
* Email verification
* OTP-based account activation
* Database integration
* API documentation
* Frontend integration
* Deployment

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Uvicorn**
* **Pydantic**
* **SQLAlchemy**
* **SQLite**
* **PostgreSQL**
* **JWT**
* **OAuth2**
* **bcrypt**
* **SMTP / Email**
* **Cloudinary**
* **React**
* **Vite**
* **REST API**

## 📚 Topics Covered

### 1. FastAPI Basics

* Installing FastAPI
* Creating a FastAPI application
* Running FastAPI with Uvicorn
* Path operations
* HTTP methods
* Route parameters
* Query parameters
* Request bodies
* Response handling

### 2. Pydantic

Learn how Pydantic is used for data validation and serialization.

* `BaseModel`
* Field validation
* Optional fields
* Nested models
* Request validation
* Response models

Example:

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int
```

### 3. REST API

Understanding RESTful API design.

* GET
* POST
* PUT
* PATCH
* DELETE
* Status codes
* Request/response structure
* API validation

### 4. CRUD Operations

Implementing complete CRUD functionality:

```text
Create
  ↓
Read
  ↓
Update
  ↓
Delete
```

### 5. Database Integration

Working with databases using SQLAlchemy.

Topics include:

* SQLAlchemy models
* Database sessions
* ORM
* Relationships
* Queries
* CRUD with database
* SQLite
* PostgreSQL

### 6. Authentication

Implementing user authentication and authorization.

Topics include:

* User registration
* Login
* Password hashing
* Password verification
* Authentication dependencies
* Protected routes
* Admin authentication

### 7. Password Hashing

Securely storing passwords using hashing algorithms such as bcrypt.

```text
Plain Password
      ↓
   bcrypt
      ↓
Hashed Password
      ↓
    Database
```

### 8. JWT Authentication

Implementing token-based authentication using JSON Web Tokens.

```text
User Login
    ↓
Verify Credentials
    ↓
Generate JWT
    ↓
Return Token
    ↓
Access Protected Routes
```

### 9. OAuth2

Working with OAuth2 authentication flows in FastAPI.

* OAuth2PasswordBearer
* Login authentication
* Access tokens
* Protected endpoints

### 10. File Upload

Handling files through FastAPI.

* Uploading files
* `UploadFile`
* Image uploads
* File validation
* File storage

### 11. Email Verification

Implementing email-based account activation.

Example workflow:

```text
User Registration
       ↓
Generate OTP
       ↓
Send Email
       ↓
User Enters OTP
       ↓
Verify OTP
       ↓
Activate Account
```

### 12. Admin System

Building protected admin functionality.

* Admin login
* Admin authorization
* Protected admin routes
* User management

### 13. API Documentation

FastAPI automatically provides interactive API documentation.

Available documentation:

```text
/docs
/redoc
```

Swagger UI can be used to test API endpoints directly from the browser.

## 📂 Project Structure

The exact structure may evolve throughout the course, but a typical project structure is:

```text
FastAPI-A-to-Z/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   ├── routers/
│   │   ├── users.py
│   │   ├── auth.py
│   │   └── admin.py
│   │
│   └── utils/
│
├── uploads/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/FastAPI-A-to-Z.git
```

### 2. Navigate to the project

```bash
cd FastAPI-A-to-Z
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
ALGORITHM=HS256

EMAIL_HOST=your_email_host
EMAIL_PORT=587
EMAIL_USERNAME=your_email
EMAIL_PASSWORD=your_email_password

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

> Never upload `.env` or API keys to GitHub.

Add the following to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

## ▶️ Running the Application

Run the FastAPI application using Uvicorn:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```text
http://127.0.0.1:8000/redoc
```

## 🔄 Backend Architecture

The typical request flow is:

```text
Client
  ↓
FastAPI Router
  ↓
Pydantic Validation
  ↓
Business Logic
  ↓
SQLAlchemy ORM
  ↓
Database
  ↓
Response
  ↓
Client
```

## 🎯 Learning Goals

By completing this repository, I aim to understand:

* How to build REST APIs with FastAPI
* How request and response validation works
* How to perform CRUD operations
* How to integrate databases
* How SQLAlchemy ORM works
* How authentication and authorization work
* How JWT authentication works
* How OAuth2 works
* How to securely hash passwords
* How to upload files and images
* How email verification works
* How to build admin functionality
* How to connect a backend with a frontend
* How to deploy FastAPI applications

## 🚀 Future Learning

After completing the fundamentals, the next areas of focus include:

* Advanced SQLAlchemy
* Async FastAPI
* Background Tasks
* WebSockets
* Redis
* Celery
* Docker
* CI/CD
* Cloud deployment
* API testing
* Microservices
* Production-grade FastAPI architecture

## 📈 Learning Progress

```text
[✓] FastAPI Basics
[✓] REST API
[✓] Pydantic
[✓] CRUD
[✓] Database Integration
[✓] Authentication
[✓] JWT
[✓] OAuth2
[✓] Password Hashing
[✓] File Upload
[✓] Email Verification
[✓] Admin Authentication
[ ] Advanced Async Programming
[ ] Testing
[ ] Docker
[ ] CI/CD
[ ] Production Deployment
```

## 👨‍💻 Author

**HR Anik**

Computer Science & Engineering Student

Interested in:

* Backend Development
* FastAPI
* Machine Learning
* Deep Learning
* Generative AI
* LLM Applications

## ⭐ Repository Goal

This repository serves as my personal **FastAPI A-to-Z learning and practice repository**, documenting my progress from beginner-level API development to building complete backend applications.

If you find this repository useful, feel free to ⭐ the repository.
