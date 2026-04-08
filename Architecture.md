## Architecture

```mermaid
flowchart LR
    U[Client / User] --> API[Amazon API Gateway]
    API --> Q[Amazon SQS]
    Q --> L[AWS Lambda]
    L --> D[Amazon DynamoDB]
    D --> S[DynamoDB Streams]
    S --> N[Amazon SNS]
    N --> E[Email / Notification Subscriber]
```md
### Flow
1. The client sends a request through Amazon API Gateway.
2. The request is placed into Amazon SQS for decoupled processing.
3. AWS Lambda consumes messages from the queue.
4. Lambda writes order data into Amazon DynamoDB.
5. DynamoDB Streams captures table changes.
6. Amazon SNS sends notifications to downstream subscribers.
