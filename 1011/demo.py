import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2',
                          )
client = boto3.client('dynamodb')
list_tables = client.list_tables()
# print(list_tables.keys())
# print(len(list_tables['TableNames']))
# Create the DynamoDB table.
response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Code',
            'AttributeType': 'S'
        },
        {
            'AttributeName' : 'Name'
            'AttributeType' : 'S'  
        },
    ],
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName': 'Code',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'Code',
            'KeyType': 'RANGE'
        },
    ],
    Tags=[
        {
            'Key' : 'Name'
            'Value' : 'Movies'
        },
    ],
    # AttributeDefinitions=[
    #     {
    #         'AttributeName': 'username',
    #         'AttributeType': 'S'
    #     },
    #     {
    #         'AttributeName': 'last_name',
    #         'AttributeType': 'S'
    #     },
    # ],
    TableClass='STANDARD'
    DeletionProtectionEnabled=True,
    BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)