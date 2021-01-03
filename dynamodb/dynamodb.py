import json
import boto3
from boto3.dynamodb.conditions import Key

from dynamodb.constants import LOCAL_ENDPOINT_URL, PK, SK

class MyDb:
    def __init__(self, table_name, endpoint_url=None):
        dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
        self.table = dynamodb.Table(table_name)
        #print(self.table)
        #print(self.table.scan())

    def build_key_json(self, pk_value, sk_value):
        key_json = {
            PK: pk_value,
            SK: sk_value
        }
        return key_json

    def insert_item(self, item_json) -> dict:
        response = self.table.put_item(
            Item=item_json,
            ConditionExpression="#mi <> :a",
            ExpressionAttributeNames={
                '#mi': PK
            },
            ExpressionAttributeValues={
                ':a': item_json.get(PK)
            },
            ReturnValues='ALL_OLD'
        )
        return response.get('Attributes', {})

    def retrieve_item(self, pk_value, sk_value):
        response = self.table.get_item(
            Key=self.build_key_json(pk_value, sk_value)
        )
        return response.get('Item', {})

    def retrieve_items(self) -> dict:
        response = self.table.scan(
            FilterExpression="contains(#mi, :a)",
            ExpressionAttributeNames={
                '#mi': PK
            },
            ExpressionAttributeValues={
                ':a': 'movie'
            },            
        )
        return response.get('Items', [])


    def delete_item(self, pk_value, sk_value) -> dict:
        response = self.table.delete_item(
            Key=self.build_key_json(pk_value, sk_value),
            ReturnValues= 'ALL_OLD'
        )
        return response.get('Attributes', {})

    def update_item(self, pk_value, sk_value, new_value) -> dict:
        response = self.table.update_item(
            Key=self.build_key_json(pk_value, sk_value),
            UpdateExpression='SET #p = :a', 
            ExpressionAttributeNames={
                '#p': 'format'
            },
            ExpressionAttributeValues={
                ':a': new_value
            }, 
            ReturnValues= 'ALL_NEW'
        )
        print(response)
        return response.get('Attributes', {})
    
    def scan_items(self) -> dict:
        response = self.table.scan()
        return response.get('Items', [])

    def retrieve_by_PK(self, pk_value):
        response = self.table.query(
            KeyConditionExpression=Key(PK).eq(pk_value) & Key(SK).between('A', 'D'),
            FilterExpression='contains(#p, :a) and #py between :b and :c',
            ExpressionAttributeNames={
                '#p': 'publisher',
                '#py': 'publish_year'
            },
            ExpressionAttributeValues={
                ':aa': 'War',
                ':a': 'C',
                ':b': 2000,
                ':c': 2020
            }, 
        )
        return response.get('Item', {})
