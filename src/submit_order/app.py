import json
import os
import uuid
import boto3

sqs = boto3.client("sqs")
queue_url = os.environ["QUEUE_URL"]

def handler(event, context):
    body = json.loads(event.get("body", "{}"))
    order_id = str(uuid.uuid4())

    message = {
        "orderId": order_id,
        "customer": body.get("customer", "unknown"),
        "product": body.get("product", "unknown"),
        "status": "RECEIVED"
    }

    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(message)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Order received",
            "orderId": order_id
        })
    }
