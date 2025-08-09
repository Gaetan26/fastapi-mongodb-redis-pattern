# FastAPI + MongoDB + Redis Pattern

A ready-to-use backend architecture pattern using FastAPI for the API, Beanie as the ODM for MongoDB, and Redis for caching.
This repository serves as a foundation for quickly building high-performance and maintainable applications.

---

## ✨ Features

- Asynchronous API with FastAPI
- MongoDB model management with Beanie
- Fast cache and sessions with Redis
- Clean and modular architecture

---

## 📂 Project Structure

```
app/
├── core/ # Configuration, constants, and global dependencies
├── logs/ # Log management and configuration
├── models/ # Beanie models (MongoDB)
├── routes/ # API endpoints
├── services/ # Business logic and integrations
├── utils/ # Utility functions
├── .env.example # Example environment variables
main.py # FastAPI entry point
tests/ # Unit Tests
requirements.txt # Python Dependencies
```

---

## 🚀 Installation

1. **Clone the Repository**
```bash
git clone https://github.com/<your-username>/fastapi-mongodb-redis-pattern.git
cd fastapi-mongodb-redis-pattern
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Environment Variables**
Create an `.env` file based on `.env.example`:
```env
MONGO_URI=mongodb://localhost:27017/
REDIS_SERVER=localhost
REDIS_PORT=6379
```

4. **Start the Server**
```bash
uvicorn main:app --reload
```

---

## 🛠 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Beanie](https://beanie-odm.dev/)
- [MongoDB](https://www.mongodb.com/)
- [Redis](https://redis.io/)

---

## 📜 License

This project is licensed under the **MIT** License – you are free to use, modify, and share it.
