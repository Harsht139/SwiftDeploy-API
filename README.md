# SwiftDeploy-API

A FastAPI-based RESTful API service that provides basic functionality and serves as a template for building scalable web services.

## Table of Contents

- [API Overview](#api-overview)
- [Local Development](#local-development)
- [Running with Docker](#running-with-docker)
- [Running Tests](#running-tests)
- [Pre-commit Hooks](#pre-commit-hooks)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## API Overview

### Available Endpoints

- **`GET /`**: Welcome message
  ```json
  {
    "message": "Welcome to the API!"
  }
  ```

- **`GET /status`**: Returns the health status of the API
  ```json
  {
    "status": "ok"
  }
  ```

- **`GET /process/{item_id}`**: Checks if a number is even or odd
  - **Path Parameter**: `item_id` (integer, required)
  - **Response Example**:
    ```json
    {
      "item_id": 42,
      "is_even_or_odd": "even"
    }
    ```

## Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/SwiftDeploy-API.git
   cd SwiftDeploy-API
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   uvicorn src.main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`

## Running with Docker

1. **Build the Docker image**:
   ```bash
   docker build -t swiftdeploy-api .
   ```

2. **Run the Docker container**:
   ```bash
   docker run -d -p 8080:8080 --name swiftdeploy-api swiftdeploy-api
   ```

The API will be available at `http://localhost:8080`

## Running Tests

To run the test suite, use `pytest`:

```bash
pytest tests/
```

## Pre-commit Hooks

This project uses `pre-commit` for code quality.

1. **Install pre-commit**:
   ```bash
   pip install pre-commit
   ```

2. **Install the git hooks**:
   ```bash
   pre-commit install
   ```

The hooks will now run automatically on every `git commit`.

## Deployment

This project includes a CI/CD pipeline using GitHub Actions to automatically build and deploy the application to Google Cloud Run whenever changes are pushed to the `main` branch.

### Prerequisites

1. A Google Cloud Project with Cloud Run API enabled
2. A service account with the following roles:
   - Cloud Run Admin
   - Service Account User
   - Storage Admin

### Setup GitHub Secrets

Add the following secrets to your GitHub repository (Settings > Secrets > Actions):

1. `GCP_PROJECT_ID`: Your Google Cloud project ID
2. `GCP_SA_KEY`: The JSON key of your Google Cloud service account

### Deployment Workflow

The deployment is handled automatically by GitHub Actions. The workflow:

1. Triggers on push to `main` branch
2. Sets up Google Cloud credentials
3. Builds a Docker image
4. Pushes the image to Google Container Registry
5. Deploys the new image to Cloud Run

### Manual Deployment

If you need to deploy manually, you can use the following commands:

1. **Build and push the Docker image**:
   ```bash
   gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/swiftdeploy-api
   ```

2. **Deploy to Cloud Run**:
   ```bash
   gcloud run deploy swiftdeploy-api \
     --image gcr.io/YOUR_PROJECT_ID/swiftdeploy-api \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

### Environment Variables

To set environment variables in Cloud Run:

1. **Via Console**: Go to Cloud Run > your-service > Edit and Deploy New Revision > Variables & Secrets
2. **Via CLI**:
   ```bash
   gcloud run services update swiftdeploy-api \
     --update-env-vars KEY1=value1,KEY2=value2 \
     --platform managed \
     --region us-central1
   ```

### Viewing Logs

1. **Via Console**: Go to Cloud Run > your-service > Logs
2. **Via CLI**:
   ```bash
   gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=swiftdeploy-api" --limit=50
   ```

## Project Structure

```
SwiftDeploy-API/
├── Dockerfile           # Docker configuration
├── requirements.txt     # Project dependencies
├── src/                 # Source code
│   ├── __init__.py
│   └── main.py         # Main application file
└── tests/              # Test files
    ├── __init__.py
    └── test_main.py    # Test cases
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

