import json
import os
import uuid
from datetime import datetime, timezone

import boto3

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

TABLE_NAME = os.environ.get("TABLE_NAME", "orders")
TOPIC_ARN = os.environ.get("TOPIC_ARN", "")

table = dynamodb.Table(TABLE_NAME)


def lambda_handler(event, context):
    results = []

    for record in event.get("Records", []):
        try:
            body = json.loads(record["body"])

            order_id = body.get("order_id", str(uuid.uuid4()))
            customer_id = body.get("customer_id", "unknown")
            amount = body.get("amount", 0)
            status = "processed"
            created_at = datetime.now(timezone.utc).isoformat()

            item = {
                "order_id": order_id,
                "customer_id": customer_id,
                "amount": amount,
                "status": status,
                "created_at": created_at
            }

            table.put_item(Item=item)

            if TOPIC_ARN:
                sns.publish(
                    TopicArn=TOPIC_ARN,
                    Subject="Order Processed",
                    Message=json.dumps({
                        "message": "Order processed successfully",
                        "order_id": order_id,
                        "customer_id": customer_id,
                        "amount": amount,
                        "status": status
                    })
                )

            results.append({
                "order_id": order_id,
                "status": "success"
            })

        except Exception as e:
            results.append({
                "status": "error",
                "error": str(e)
            })

    return {
        "statusCode": 200,
        "body": json.dumps(results)
    }
