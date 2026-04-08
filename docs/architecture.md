# Architecture

```mermaid
flowchart LR
  A[Client] --> B[API Gateway]
  B --> C[SubmitOrder Lambda]
  C --> D[SQS Queue]
  D --> E[ProcessOrder Lambda]
  E --> F[DynamoDB]
  E --> G[SNS Topic]
