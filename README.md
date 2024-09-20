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

2. **Create a `.env` file:**

   Create a `.env` file in the root directory of the project based on .env.example

3. **Build & run the Docker image:**

   ```bash
   docker-compose up --build
   ```
4. **Run initial migrations:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate 
   pip install -r requirements.txt
   alembic upgrade head
   ```

5. **Access the API:**

   The API is now accessible at [http://localhost:8000/docs](http://localhost:8000/docs).

### BONUS QUESTION: 
If we are going to deploy this on production, what do you think is the next improvement that you will prioritize next?
```
- I will prioritize the following improvements:
  - **Monitoring:** Set up monitoring tools to track the performance and health of the application.
  - **Logging:** Implement logging to track and debug issues in the application.
  - **Caching:** Implement caching to improve the performance of the application.
  - **Testing:** Write unit tests, integration tests, and end-to-end tests to ensure the reliability of the application.
  - **CI/CD:** Set up continuous integration and continuous deployment pipelines to automate the deployment process.
  - **Documentation:** Improve the documentation to make it easier for developers to understand and contribute to the project.
  - **Error Handling:** Implement error handling to provide meaningful error messages to users and developers.
  - **Optimization:** Optimize the application for performance and efficiency to reduce response times and resource usage.
  - **Database Optimization:** Optimize the database queries and schema to improve the performance of the application.
```
