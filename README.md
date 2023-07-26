# Machine Learning Model Deployment

This project deploys machine learning models via a web API using Django. It has the following key features:

- Serves multiple ML models and versions through the same API endpoint
- Stores request information for model testing and auditing 
- Includes A/B testing capabilities
- Full test suite for ML and server code
- Docker setup for containerization

## Code Structure

- `research/` - ML model training code and A/B testing simulation code 
- `backend/` - Django web application
- `docker/` - Dockerfiles for containerization

The ML models are trained on the [Adult Income dataset](https://archive.ics.uci.edu/dataset/2/adult).

## Getting Started

To run locally:

1. Clone the repo
2. Install requirements
3. Run Django development server

To deploy in production:

1. Build Docker image 
2. Run image in container with port mapping

## Models

The API currently supports the following ML models:

- Random Forest
- Exit Trees

See the code for details on model versions and endpoints.

## Contributing

Contributions are welcome! Open an issue or PR to suggest additions or fixes.

## About

This project was created by Daniil Pokryshkin to demonstrate machine learning model deployment with Django. Let me know if you have any feedback!
