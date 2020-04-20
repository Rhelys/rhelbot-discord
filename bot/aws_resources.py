# aws_resources.py

import boto3
import json
import decimal
import socket

from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError


dynamodb = boto3.resource("dynamodb", region_name='us-west-2', endpoint_url="http://localhost:8000")
whitelist_table = dynamodb.Table('rhelbot-discord')


def fetch_bot_token():
    local_hostname = socket.gethostname()
    if local_hostname == 'Din':
        boto_session = boto3.Session(profile_name='rhelbot')
        s3_token = boto_session.client('s3')

    else:
        s3_token = boto3.client('s3')

    s3_token.download_file('rhelbot-discord', "rhelbot_token.txt", "rhelbot_token.txt")


def fetch_server_welcome(server_id):
    try:
        ddb_response = whitelist_table.get_item(
            Key={
                'server_id': server_id
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        print(f'This server has not been onboarded to the bot config yet')
        return 'Error'
    else:
        server_entry = ddb_response['Item']
        return str(server_entry['welcome_message'])


# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


