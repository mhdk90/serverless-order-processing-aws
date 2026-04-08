\# Serverless Order Processing on AWS



\## Overview

This project demonstrates an event-driven serverless architecture on AWS using API Gateway, Lambda, SQS, DynamoDB, and SNS.



\## Goal

Build a simple order-processing workflow that accepts orders through an API, processes them asynchronously, stores them in DynamoDB, and publishes notifications.



\## Architecture

1\. API Gateway receives a POST request

2\. Lambda function sends the order to SQS

3\. A second Lambda function reads from SQS

4\. The processed order is stored in DynamoDB

5\. SNS publishes a notification



\## Files

\- `template.yaml` – AWS SAM template for the serverless architecture

\- `docs/` – project notes and later architecture diagrams



\## Services Used

\- Amazon API Gateway

\- AWS Lambda

\- Amazon SQS

\- Amazon DynamoDB

\- Amazon SNS

\- AWS SAM



\## What I Learned

\- How to design event-driven AWS architectures

\- How to decouple services with SQS

\- How to define serverless infrastructure in YAML

\- How to document cloud projects for GitHub and CV use

