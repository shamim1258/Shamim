```
import boto3
import botocore.exceptions
import logging
import os
from os import path
import json
import csv

def lambda_handler(event, context):
    filename = ""
	destination_bucket = 'kpn-voip-update-input-prod'
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
	try:
		for record in event['Records']:
			bucket = record['s3']['bucket']['name']
			key = record['s3']['object']['key']
		filename = str(key)
		os.chdir('/tmp/')
		s3.Bucket(bucket).download_file(key,filename)
		print("List files in tmp directory ::",os.listdir())
		s3_client.upload_file(key,destination_bucket,filename, ExtraArgs={'ServerSideEncryption': 'AES256'})
	except Exception as err:
		print("Exception :: ",err)
    
    return {
        'statusCode': 200,
        'body': json.dumps(filename)
    }
```
