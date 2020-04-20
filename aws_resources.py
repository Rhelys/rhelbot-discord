# aws_resources.py

import boto3
import json
import decimal
import socket

from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


def fetchBotToken():
    localHostname = socket.gethostname()
    if localHostname == 'Din':
        botoSession = boto3.Session(profile_name='rhelbot')
        s3_token = botoSession.client('s3')

    else:
        s3_token = boto3.client('s3')

    s3_token.download_file('rhelbot-discord', "rhelbot_token.txt", "rhelbot_token.txt")


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource("dynamodb", region_name='us-west-2', endpoint_url="http://localhost:8000")


whitelistTable = dynamodb.Table('rhelbot-discord')