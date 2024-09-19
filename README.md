# FastAPI Backend Setup

This project is a FastAPI-based backend application that uses Docker and Docker Compose for easy setup and management. Follow the instructions below to get started.

## Prerequisites

Ensure that you have the following installed on your local machine:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hicarlodacuyan/sprout-exam-backend.git
   cd sprout-exam-backend
   ```

2. **Build & run the Docker image:**

   ```bash
   docker-compose up --Build
   ```
3. **Run initial migrations:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate 
   pip install -r requirements.txt
   alembic upgrade head
   ```

4. **Access the API:**

   The API is now accessible at [http://localhost:8000/docs](http://localhost:8000/docs).


