import logging

import azure.functions as func

import os
import re
import uuid

import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey
import datetime

HOST = 'https://coen241-group2-cosmosdb.documents.azure.com:443/'
MASTER_KEY = 'RAQWGFqiniMmSACH4goJU8kgJuISDwX1TttSWh6C9gDlh36xwnucmjWNYDMDEi9coYGpW4qgkF4tDHmdeYTXjw=='
DATABASE_ID = 'COEN241'
CONTAINER_ID = 'Containers'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    client = cosmos_client.CosmosClient(HOST, { 'masterKey': MASTER_KEY })
    try:
        database = client.get_database_client(DATABASE_ID)
        container = database.get_container_client(CONTAINER_ID)
    except exceptions.CosmosHttpResponseError:
        logging.info("exception")
        return func.HttpResponse("Cannot get connections")

    p = re.compile('[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}')
    # get files in /tmp folder
    files = os.listdir('/tmp')
    # get if there's a uuid file
    used = [ str(s) for s in files if p.match(s) ]

    if len(used) > 0:
        logging.info(used)
        return func.HttpResponse("Success", status_code = 200)

    containerId = str(uuid.uuid4())
    open(f"/tmp/{containerId}", "x")
    container.create_item(body = {
        'id': str(uuid.uuid4()),
        'uuid': containerId,
    })

    logging.info(containerId)
    return func.HttpResponse("Success", status_code = 200)

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
