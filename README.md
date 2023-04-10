# OpenAI Token Estimator

This is a Python microservice API that accepts JSON requests and can be used to estimate the number of tokens in OpenAI API requests. It is based on the [tiktoken](https://github.com/openai/tiktoken) library.

## Features

- Estimate the number of tokens for a given text input
- Useful for planning usage and cost optimization with the OpenAI API
- Simple and easy-to-use API

## Getting Started

### Installation

1. Clone the repository
2. Navigate to the project directory
3. Install the required packages: `pip install -r requirements.txt`

### Running the API locally

1. Set the API key as an environment variable: `set API_KEY=my-key` (Replace `my-key` with your actual API key.
)
2. uvicorn web_service:app --reload

There is a run_local.bat script that will do the same for you. 

This will start the API server at `http://127.0.0.1:8000`.

## Docker

A Docker image is available on Docker Hub. To use it, follow these steps:

1. Pull the Docker image: `docker pull pavlass2/token_calculator:1.0`
2. Run the Docker container: `docker run -p 8000:8000 -e API_KEY=my-key pavlass2/token_calculator:1.0`

Replace `my-key` with your actual API key.

Again this will start the API server at `http://127.0.0.1:8000`.