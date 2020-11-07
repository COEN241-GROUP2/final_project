import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(
    TableName = 'Metric',
    KeySchema = [
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
    ],
    BillingMode = 'PAY_PER_REQUEST',
)