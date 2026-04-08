import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

table = dynamodb.Table(os.environ["TABLE_NAME"])
topic_arn = os.environ["TOPIC_ARN"]

def handler(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])

        item = {
            "orderId": body["orderId"],
            "customer": body["customer"],
            "product": body["product"],
            "status": "PROCESSED"
        }

        table.put_item(Item=item)

        sns.publish(
            TopicArn=topic_arn,
            Subject="Order Processed",
            Message=json.dumps(item)
        )

    return {"statusCode": 200}
