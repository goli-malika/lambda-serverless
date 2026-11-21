# Student Information - Serverless API

## Project Overview
A simple Student Information API developed using a Python Lambda-style handler.

## Technologies
- Python
- AWS Lambda concepts
- Amazon API Gateway concepts
- JSON

## API Endpoints

### GET /students
Returns student information.

Expected Status: 200

### POST /students
Accepts student information and returns a success response.

Expected Status: 201

## Architecture
Client → API Gateway → AWS Lambda → JSON Response

## Testing
The API Gateway event and Lambda handler workflow was simulated locally using Python.

## Result
Successfully tested GET and POST request handling locally.

**Note:** This is a local simulation. Actual AWS Lambda and API Gateway deployment has not been performed.
