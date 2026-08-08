# Flask API and MongoDB Assignment

## Project Overview

This repository contains two Flask-based assignments:

### Assignment 1: Flask API Project

- Create a Flask application with an `/api` route.
- Read data from a backend JSON file.
- Return the data as a JSON response.

### Assignment 2: Flask MongoDB Project

- Create a frontend form using Flask.
- Submit data to MongoDB Atlas.
- Redirect the user to a success page after successful submission.

---

# Project Structure

```text
Flask_MongoDB_Assignment/
│
├── flask_api_project/
│   ├── app.py
│   └── data.json
│
├── flask_mongodb/
│   ├── app.py
│   └── templates/
│       ├── form.html
│       └── success.html
│
├── .env
├── .gitignore
├── install.sh
├── Readme.md
└── requirements.txt
```

---

# Technologies Used

- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML
- Git
- GitHub

---

# Prerequisites

Before running the project, ensure the following are installed:

- Python 3.x
- pip
- Git
- MongoDB Atlas Account

Verify installation:

```bash
python --version
pip --version
git --version
```

---

# Install Dependencies

Install all required packages:

```
Contents of requirements.txt:
```
```txt
Flask>=2.2,<3
pymongo>=4.4,<5
python-dotenv>=1.0.0
gunicorn>=20.1.0
```
---

# Install Script (All of the inatallation packages are in requirements.txt file)

Run:

```bash
chmod +x install.sh
./install.sh
```

Purpose:

- Installs required Python packages
- Simplifies project setup

---

# MongoDB Atlas Configuration

## Step 1: Create Cluster

- Login to MongoDB Atlas
- Create a free M0 Cluster

## Step 2: Create Database User

Navigate to:

```text
Security → Database Access
```

Create a database user.

Example:

```text
Username: admin
Password: ********
```

## Step 3: Configure Network Access

Navigate to:

```text
Security → Network Access
```

Add:

```text
0.0.0.0/0
```

## Step 4: Copy Connection String

Navigate to:

```text
Cluster → Connect → Drivers → Python
```

Example:

```text
mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
```

---

# Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority
```

---

# Assignment 1: Flask API Project

## Files

```text
flask_api_project/
│
├── app.py
└── data.json
```

## Run Application

Navigate to:

```bash
cd flask_api_project
```

Run:

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:5000
```

API Endpoint:

```text
http://127.0.0.1:5000/api
```

### Expected Output

```json
[
  {
    "course": "Python",
    "id": 1,
    "name": "Gyani"
  },
  {
    "course": "Flask",
    "id": 2,
    "name": "Ganesh"
  }
]
```

---

# Assignment 2: Flask MongoDB Project

## Files

```text
flask_mongodb/
│
├── app.py
│
└── templates/
    ├── form.html
    └── success.html
```

## Run Application

Navigate to:

```bash
cd flask_mongodb
```

Run:

```bash
python app.py
```

Application URL:

```text
http://127.0.0.1:5001
```

---

# Application Workflow

1. User opens the form page.
2. User enters Name and Email.
3. Form submits data to Flask.
4. Flask inserts the data into MongoDB Atlas.
5. User is redirected to the success page.
6. Data is stored in the MongoDB collection.

---

# Verify MongoDB Data

Open MongoDB Atlas:

```text
Database → Browse Collections
```

Expected Database:

```text
studentdb
```

Expected Collection:

```text
students
```

Example Document:

```json
{
  "_id": "ObjectId(...)",
  "name": "Gyaneshwar Sharma",
  "email": "gyaneshwar@example.com"
}
```

---

# Git Commands

Initialize repository:

```bash
git init
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Completed Flask API and MongoDB Assignments"
```

Connect GitHub repository:

```bash
git remote add origin <repository-url>
```

Push code:

```bash
git branch -M main
git push -u origin main
```

---

# Project Assignment document with Screenshots

Include screenshots of:

1. Project Structure in VS Code
2. Flask API Running in Terminal
3. API JSON Output
4. MongoDB Form Page
5. Success Page
6. MongoDB Atlas Collection
7. GitHub Repository

---

# Learning Outcomes

After completing this assignment, I learned:

- Flask routing and templates
- Reading JSON files in Flask
- Creating REST API endpoints
- MongoDB Atlas configuration
- Using PyMongo with Flask
- Handling form submissions
- Redirecting users between pages
- Using environment variables securely
- Version control using Git and GitHub

---

# Author

Gyaneshwar Sharma
