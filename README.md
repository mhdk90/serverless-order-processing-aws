# Serverless Order Processing on AWS

## Overview
This project demonstrates an event-driven serverless architecture on AWS using API Gateway, Lambda, SQS, DynamoDB, and SNS.

## Goal
Build a simple order-processing workflow that accepts orders through an API, processes them asynchronously, stores them in DynamoDB, and publishes notifications.

## Current Scope
- AWS SAM template
- Event-driven serverless workflow
- Order submission and processing flow

## Repository Structure
- `template.yaml` – main AWS SAM template
- `docs/` – notes and architecture explanations

## Planned Next Steps
- Move Lambda code into separate `src/` folders
- Add sample request JSON
- Add architecture diagram
- Add deployment and cleanup steps

## Services Used
- Amazon API Gateway
- AWS Lambda
- Amazon SQS
- Amazon DynamoDB
- Amazon SNS
- AWS SAM

## Security Notes
- No real secrets are stored in this repository
- Environment-specific values should be passed securely at deploy time
