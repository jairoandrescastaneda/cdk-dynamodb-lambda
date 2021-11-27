import json
import boto3
import os
from logging import basicConfig, getLogger, INFO

logger = getLogger(__name__)
basicConfig(level=INFO)

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ["TABLE_NAME"]


def handler(event, context):
    user_info = json.loads(event["body"])
    user_table = dynamodb.Table(TABLE_NAME)
    logger.info(user_info)
    response = user_table.put_item(Item=user_info)
    logger.info("User created")
    logger.info(response)

    return {"statusCode": 200}
