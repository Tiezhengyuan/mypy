import unittest
import boto3
from moto import mock_dynamodb2
import pytest

from dynamodb.constants import *
import dynamodb.dynamodb as db
from conftest import dynamodb_table

'''
@mock_dynamodb2
def test_insert_item():
    print("test insert_item()")
    dynamodb_table()
    
    #test an item
    response = db.MyDb(LOCAL_TABLE_NAME).insert_item(MOVIE1)
    assert response == {}

    #test an duplicate item
    with pytest.raises(Exception) as err:
        db.MyDb(LOCAL_TABLE_NAME).insert_item(MOVIE1)

@mock_dynamodb2
def test_get_item():
    print("test get_item()")
    dynamodb_table()

    expected = MOVIE0[PK]
    response = db.MyDb(LOCAL_TABLE_NAME).retrieve_item(expected, MOVIE0[SK])
    assert response[PK] == expected

@mock_dynamodb2
def test_get_items():
    print("test get_items()")
    dynamodb_table()

    response = db.MyDb(LOCAL_TABLE_NAME).retrieve_items()
    assert len(response) == 1


@mock_dynamodb2
def test_delete_item():
    print("test delete_item()")
    dynamodb_table()

    response = db.MyDb(LOCAL_TABLE_NAME).delete_item(MOVIE0[PK], MOVIE0[SK])
    print(response)
'''
@mock_dynamodb2
def test_update_item():
    print("test update_item")
    dynamodb_table()

    expected = 'mp4'
    response = db.MyDb(LOCAL_TABLE_NAME).update_item(\
        MOVIE0[PK], MOVIE0[SK], expected)
    assert response['format'] == expected

'''
@mock_dynamodb2
def test_scan_items():
    print("test scan_items")
    dynamodb_table()

    response = db.MyDb(LOCAL_TABLE_NAME).scan_items()
    assert len(response) == 1


@mock_dynamodb2
def test_retrieve_by_PK():
    print("test table query")
    dynamodb_table()

    response = db.MyDb(LOCAL_TABLE_NAME).retrieve_by_PK(MOVIE0[PK])
'''