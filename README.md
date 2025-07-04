# 🤖 QASystem

A simple, production-ready **question-answering system** that enables users to send questions via a REST API and receive intelligent answers powered by **OpenAI's gpt-4o-mini**.

---

## ✨ Features

- **🧠 Question Answering:** Submit a question to the `/query/` endpoint and receive an AI-generated response.
- **💱 Currency Conversion Assistant:** Ask natural language currency conversion queries (e.g., "Convert 100 USD to EUR") via the `/currency/` endpoint, backed by OpenAI function calling.
- **📦 Product Info Extraction:** Extract structured product metadata from free-form descriptions using the `/extract-product/` endpoint.
- **🧩 OpenAI Tool Calling:** Utilizes OpenAI's function calling capabilities to invoke structured tools like currency conversion and data extraction.
- **⚡ FastAPI-Powered:** Asynchronous, high-performance REST API using FastAPI.
- **🌐 NGINX Reverse Proxy:** Routes incoming requests through NGINX for improved performance and production readiness.
- **🔐 Secure Configuration:** API keys and secrets managed through environment variables.
- **🛡️ Local HTTPS Support:** Supports SSL via self-signed certificates for secure local development over HTTPS.
- **🔄 GitHub Actions CI/CD:** Automatically builds and pushes Docker images to Docker Hub (`dhiraj918106/qasystem`) on every push to `main`.
- **🌐 CORS Enabled:** Fully accessible from browser-based tools like Swagger UI.
- **📦 Containerized Deployment:** Easily deployable with Docker and Gunicorn/Uvicorn for production.
- **📝 Basic Logging:** Tracks API requests, responses, and errors using Python’s logging module.

---

## 📊 Tech Stack

* **FastAPI** — REST API framework with built-in async support and auto-generated docs.
* **OpenAI API** — Uses `gpt-4o-mini` to generate intelligent answers and execute tool calls.
* **Gunicorn + Uvicorn** — ASGI production server combination for scalable performance.
* **python-dotenv** — Manage configuration securely using `.env` files.
* **Docker + Docker Compose** — Containerized, portable deployment.
* **NGINX** — Acts as a reverse proxy in front of the FastAPI service for routing and scalability.
* **OpenSSL** — Used to generate self-signed certificates for HTTPS support in local development.
* **GitHub Actions** — CI/CD pipeline that builds and pushes images to Docker Hub automatically.
