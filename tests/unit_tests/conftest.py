import unittest
import pytest
import boto3
from moto import mock_dynamodb2

from dynamodb.constants import LOCAL_TABLE_NAME, MOVIE0


def pytest_runtest_setup():
    print("\n\t>>>New test:")


@mock_dynamodb2
def dynamodb_table():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName = LOCAL_TABLE_NAME, 
        KeySchema=[
            {
                'AttributeName': 'movie_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'movie_name',
                'KeyType': 'RANGE'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'movie_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'movie_name',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
        )
    table.put_item(Item=MOVIE0)
    #table.meta.client.get_waiter('table_exists').wait(TableName='surveys')
    #print(table.scan())
    return table


def delete_table():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(LOCAL_TABLE_NAME)
    table.delete(0)