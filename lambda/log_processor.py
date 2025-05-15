import json
import boto3
import gzip
import os

sqs = boto3.client('sqs')
QUEUE_URL = os.environ['SQS_URL']

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        s3 = boto3.client('s3')
        obj = s3.get_object(Bucket=bucket, Key=key)

        content = gzip.decompress(obj['Body'].read()).decode('utf-8')
        lines = content.strip().split('\n')

        for line in lines:
            log = json.loads(line)
            sqs.send_message(QueueUrl=QUEUE_URL, MessageBody=json.dumps(log))

    return {
        'statusCode': 200,
        'body': json.dumps('Log processing complete.')
    }
