import boto3

tname1 = 'Mac_Address';
tname2 = 'ONID';
tname3 = 'Records';

# access DynamoDB
dynamodb = boto3.client('dynamodb')

# create table 1
table = dynamodb.create_table(
    # set name of table
    TableName = tname1,
    # set information about attribute
    KeySchema = [
        {
            'AttributeName': 'PIN',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'PIN',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# create table 2
table = dynamodb.create_table(
    TableName = tname2,
    KeySchema = [
        {
            'AttributeName': 'PIN',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'PIN',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# create table 3
table = dynamodb.create_table(
    TableName = tname3,
    KeySchema = [
        {
            'AttributeName': 'PIN',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions = [
        {
            'AttributeName': 'PIN',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput = {
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
