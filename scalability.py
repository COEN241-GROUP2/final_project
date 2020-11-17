import json
import os
import uuid
import boto3
import re

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    p = re.compile('[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
    # get files in /tmp folder
    files = os.listdir('/tmp')
    # get if there's a uuid file
    used = [ str(s) for s in files if p.match(s) ]
    
    response = {
        'statusCode': 200
    }
    
    if len(used) > 0:
        return response
    
    # get dynamodb table
    containerId = str(uuid.uuid4())
    f = open(f"/tmp/{containerId}", "x")
    metricTable = dynamodb.Table('Metric')
    metricTable.put_item(
        Item = {
            'id': str(uuid.uuid4()),
            'containerId': containerId,
        }
    )
    
    return response
