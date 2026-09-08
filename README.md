# 🛡️ Real-Time Fraud Detection API & Streaming Pipeline

An enterprise-grade, real-time fraud detection engine built with **Python, FastAPI, Machine Learning (Scikit-Learn IsolationForest), Apache Kafka, Redis, and PostgreSQL**.

Evaluates financial transactions in real-time by combining **deterministic rule-based heuristic risk scoring** (amount thresholds, geo-velocity/high-risk country checks, device novelty) with **unsupervised machine learning anomaly detection** trained on historical credit card transaction data.

---

## ✨ Features

- **🚀 High-Performance REST API**: Powered by FastAPI & Uvicorn with async I/O for sub-50ms transaction risk evaluation.
- **🧠 Hybrid Fraud Engine**: Combines deterministic business rule heuristics with Scikit-Learn `IsolationForest` anomaly detection.
- **⚡ Event-Driven Streaming**: Real-time event pipeline using Apache Kafka (KRaft mode v4.0) to stream, score, and persist high-volume transaction feeds asynchronously.
- **⚡ High-Speed Caching**: In-memory caching with Redis 7 for instant risk flag lookup and state tracking.
- **💾 Asynchronous Persistence**: Database ORM built with SQLAlchemy and AsyncPG targeting PostgreSQL 17.
- **🐳 Multi-Container Orchestration**: Fully containerized with Docker & Docker Compose.
- **📬 Postman Ready**: Includes pre-built Postman Collection (`Fraud_Detection_API.postman_collection.json`) and Environment config.

---

## 🏗️ Architecture

```
[ Client / Web App / Script ] ───► POST /transactions/ ───► [ FastAPI Engine ]
                                                                   │
                                                                   ├──► [ Heuristic Rules Engine ]
                                                                   ├──► [ ML IsolationForest Model ]
                                                                   ├──► [ Redis Cache ]
                                                                   └──► [ PostgreSQL Database ]

[ Simulated Generator ] ───► [ Apache Kafka Topic: 'transactions' ] ───► [ Kafka Consumer Worker ]
```

---

## 🛠️ Tech Stack

| Technology                           | Purpose                                          |
| :----------------------------------- | :----------------------------------------------- |
| **FastAPI + Uvicorn**                | Asynchronous RESTful API framework               |
| **Scikit-Learn (`IsolationForest`)** | Unsupervised ML anomaly detection model          |
| **Apache Kafka (KRaft)**             | Distributed event streaming broker               |
| **Redis 7**                          | Sub-millisecond in-memory cache                  |
| **PostgreSQL 17 + AsyncPG**          | Persistent database storage via SQLAlchemy Async |
| **Docker & Docker Compose**          | Microservice containerization and orchestration  |

---

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.10+
- Docker & Docker Compose

### 1. Start Infrastructure Containers

```bash
docker-compose up -d postgres redis kafka
```

### 2. Set Up Virtual Environment & Install Dependencies

```bash
python -m venv venv

# On Windows PowerShell:
.\venv\Scripts\Activate.ps1

# On Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run the FastAPI Application

```bash
uvicorn app.main:app --reload --port 8000
```

- Interactive Swagger UI: `http://localhost:8000/docs`
- ReDoc API Documentation: `http://localhost:8000/redoc`

### 4. Run Kafka Streaming Pipeline (Optional)

In separate terminal windows:

```bash
# Terminal 1: Start Kafka Consumer
python app/kafka/consumer.py

# Terminal 2: Start Kafka Producer (simulates real-time transaction stream)
python app/kafka/producer.py
```

---

## 🧪 API Usage & Example Request

### `POST /transactions/`

#### Request Body

```json
{
  "amount": 75000.0,
  "country": "RU",
  "device": "new"
}
```

#### Response (`200 OK`)

```json
{
  "fraud_score": 95,
  "risk": "High",
  "reasons": ["Large amount", "High-risk country", "New device"]
}
```

---

## 📬 Postman Testing

Import the included files into Postman for instant manual testing:

- **Collection**: [`Fraud_Detection_API.postman_collection.json`](./Fraud_Detection_API.postman_collection.json)
- **Environment**: [`Fraud_Detection_API.postman_environment.json`](./Fraud_Detection_API.postman_environment.json)
