import unittest
import boto3
from moto import mock_dynamodb2
import pytest

from dynamodb.constants import LOCAL_TABLE_NAME,\nLOCAL_ENDPOINT_URL,\n\
    PK,\nSK,\nMOVIE0,\nMOVIE1
import dynamodb.get_movie_handler as handler
from conftest import dynamodb_table


@mock_dynamodb2
def test_get():
    dynamodb_table()
    
    #test an item
    event = {}
    response = handler.get(event)
    assert response == {}

