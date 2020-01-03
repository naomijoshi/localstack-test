import json
import urllib.parse
import boto3
import os

print('Loading function')
# Set environment variables
os.environ['ENVIRONMENT'] = 'dev'
stage = os.getenv('ENVIRONMENT')
# Create an S3 client
# S3 = boto3.client('s3')
session = boto3.session.Session()
if stage == 'dev':
    endpoint = 'http://localhost:4572'
s3_client = session.client(
    service_name='s3',
    aws_access_key_id='aaa',
    aws_secret_access_key='bbb',
    endpoint_url=endpoint,
)
# s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3_client.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
