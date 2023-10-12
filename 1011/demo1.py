import boto3


client = boto3.client('dynamoeb')
table = dynamodb.Table('Movies')
item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
client.put_item(
    TableName='Movies',Item=item    
)
item = {
    'Code' : '20050112','Name': 'Batman Begins', 
    'Time' : 134, 'Genre': '범죄 액션 판타지',
    'Date': '2005-06-24', 'Director':'크리스토퍼 놀란',
    'Actor': '리암 니슨,크리스찬 베일, 마이클 케인'
}
table.put_item(Item=item)
# client.put_item(
#     TableName='Movies', Item=item
# )    