# MLOps Lab 6 - ML Model Training & Serving Pipeline

This project demonstrates a complete MLOps pipeline using Docker and Docker Compose to train a machine learning model and serve it via a REST API.

## Project Structure

```
.
├── training/              # Model training service
│   ├── train.py          # Training script
│   ├── Dockerfile        # Training container
│   └── requirements.txt   # Training dependencies
├── serving/              # Model serving service
│   ├── app.py           # FastAPI application
│   ├── wait-for-model.sh # Health check script
│   ├── Dockerfile       # Serving container
│   └── requirements.txt  # Serving dependencies
├── model/               # Shared volume for trained model
│   └── model.pkl        # Trained model (generated)
└── docker-compose.yml   # Orchestration configuration
```

## Overview

### Training Service
The training service uses scikit-learn to train a Random Forest classifier on the Iris dataset and saves the model to a shared volume.

### Serving Service
The serving service uses FastAPI to expose a REST API endpoint that loads the trained model and performs predictions on new data.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Pipeline

1. **Build and run the complete pipeline:**
```bash
docker-compose up --build
```

This will:
- Build and run the training container
- Train the model and save it to `model/model.pkl`
- Build and run the serving container
- Start the FastAPI server on `http://localhost:8000`

2. **Make predictions:**
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

## API Endpoints

### POST `/predict`
**Request:**
```json
{
  "features": [5.1, 3.5, 1.4, 0.2]
}
```

**Response:**
```json
{
  "prediction": 0
}
```

## Key Features

- **Isolated Services**: Training and serving run in separate containers
- **Shared Volume**: Model is persisted and shared between containers
- **Service Dependencies**: API waits for model file before starting
- **Production-Ready**: Uses uvicorn for production ASGI serving
- **Health Checks**: Wait script ensures model exists before API starts

## Model Details

- **Algorithm**: Random Forest Classifier
- **Dataset**: Iris (150 samples, 4 features, 3 classes)
- **Train/Test Split**: 80/20