import json
import os
import uuid
import re

def lambda_handler(event, context):
    p = re.compile('[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
    # get files in /tmp folder
    files = os.listdir('/tmp')
    # get if there's a uuid file
    used = [ str(s) for s in files if p.match(s) ]
    print(used)
    
    response = {
        'statusCode': 200
    }
    
    return response
