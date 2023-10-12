import boto3

resource = boto3.resurce("dynamodb", region_name='ap-northeast-2',
                         aws_access_key_id='AKIA3PU7RNERTDUZL4U7',
                         aws_sercret_access_key='xr0K0wYuPzDCfhPPh7cLgarZ/VB1MKJnp+vgho2')

client = boto3.client('dynamodb')
list_tables =client.list_tab() #dict
# print(client.list_tab)
# print(len(list_tables['TableNames'])) #dict
respones = client.create_table(
TableName='Movies',
KeySchema=[    
    {
        'AttributeName':'Code',
        'AttributeType': 'S'
    }
]
)

table = client.describe_table(
    TableName = 'lab-movie'       
)
# print(table)
table = resource.Table('lab-movie')
item = {
    "Code" : '19780080',
    "Name" : 'Star Wars'
    ,"Genre" : 'SF',
    "Date": '1978-04-12',
    'Director':  'George Lucas',
    'Actor': '마크 해밀, 캐리 피셔, 해리슨 포드, 알렉 기네'
}
table.put_item(item=item)
