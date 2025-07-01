
# 🤖 QASystem

A simple, production-ready **question-answering system** that enables users to send questions via a REST API and receive intelligent answers powered by **OpenAI's gpt-4o-mini**.

---

## ✨ Features

- **🧠 Question Answering:** Submit a question to the `/query/` endpoint and receive an AI-generated response.
- **⚡ FastAPI-Powered:** Asynchronous, high-performance REST API using FastAPI.
- **🔐 Secure Configuration:** API keys and secrets managed through environment variables.
- **🌐 CORS Enabled:** Fully accessible from browser-based tools like Swagger UI.
- **📦 Containerized Deployment:** Easily deployable with Docker and Gunicorn/Uvicorn for production.
- **📝 Basic Logging:** Track requests and errors for debugging and monitoring.



## 📊 Tech Stack

* **FastAPI** — REST API framework with built-in async support and auto-generated docs.
* **OpenAI API** — Uses `gpt-4o-mini` to generate intelligent answers.
* **Gunicorn + Uvicorn** — ASGI production server combination for scalable performance.
* **python-dotenv** — Manage configuration securely using `.env` files.
* **Docker + Docker Compose** — Containerized, portable deployment.

---


