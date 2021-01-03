import json
import dynamodb.dynamodb as db
from dynamodb.constants import TABLE_NAME, PK, SK

def get(event, context):
    print(event)
    body = {
        "message": "GET! No return!",
        "input": event,
    }

    if "queryStringParameters" in event:
        #get an item
        pk_value = event["queryStringParameters"].get(PK)
        sk_value = event["queryStringParameters"].get(SK)
        if pk_value and sk_value:
            result = db.MyDb(TABLE_NAME).retrieve_item(pk_value, sk_value)
            response = {
                "statusCode": 200,
                'body': json.dumps(result)
            }
            return response

        #get items
        pk_value = event["queryStringParameters"].get('items')
        if pk_value in ('movie', None):
            result = db.MyDb(TABLE_NAME).retrieve_items()
            response = {
                "statusCode": 200,
                'body': json.dumps(result)
            }
            return response

    response = {
        "statusCode": 500,
        "body": json.dumps(body)
    }

    return response

