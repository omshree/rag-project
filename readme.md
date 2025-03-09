

## Overview

This project is a Fsimple RAG application for ubuntu documentation.
---

## How to Use the Dockerfile & Run the Application

### **1 Build the Docker Image**

Run the following command to build the Docker image:

```bash
docker build -t my-fastapi-app .
```

### **2️ Run the Docker Container**

To start the application in a container, execute:

```bash
docker run -p 8000:8000 my-fastapi-app
```

Now the FastAPI application will be running at [**http://localhost:8000**](http://localhost:8000).

### **3️ Stop the Container**

To stop the running container, use:

```bash
docker ps  # Find the container ID
docker stop <container_id>
```

---

## Cloning & Setting Up the Application Manually

### **1️ Clone the Repository**

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### **2️ Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️ Run the Application**

```bash
python src/run.py
```

---

## Testing FastAPI & Swagger Integration

You can manually run the FastAPI app using **Uvicorn** and test the API using Swagger.

### **1 Start FastAPI with Uvicorn for RAG application**

```bash
uvicorn app:app --reload --loop asyncio
```
### **2 Start FastAPI with Uvicorn for E comm application**

```bash
uvicorn ecom_app:app --reload --loop asyncio
```

### **3 Access API Documentation**

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc UI**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

This allows you to interact with API endpoints directly from the browser.

---
