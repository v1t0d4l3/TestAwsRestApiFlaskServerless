# User Management Flask API

This repository contains the source code and configuration for a serverless Flask API designed for user management, using AWS services. The project utilizes the Serverless Framework to simplify deployment and management. Below is a detailed guide on the project structure, configuration, and deployment process.

## Project Structure

The project structure is organized as follows:

- **`serverless.yml`**: This file contains the configuration for the Serverless Framework, defining AWS resources, functions, and settings.
- **`app.py`**: This file contains the REST API code.
- **`requirements.txt`**: Lists the Python packages required for the application.
- **`README.md`**: This documentation file.

## Deployment

To deploy the project, follow these steps:

- **Install Serverless Framework**: If not already installed, run `npm install -g serverless` to install the Serverless Framework globally.
- **Configure AWS Credentials**: Set up AWS credentials.
- **Install Dependencies**: Run `npm install` to install the required Serverless plugins.
- **Deploy**: Execute `serverless deploy` to deploy the Flask API and DynamoDB table to AWS.
- **Access Endpoints**: After deployment, Serverless will provide endpoints for your functions. You can find them in the output after deployment.