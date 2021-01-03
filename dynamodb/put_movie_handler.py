import json
import dynamodb.dynamodb as db
from dynamodb.constants import TABLE_NAME, PK, SK

def put(event, context):
    print(event)
    body = {
        "message": "PUT! No return!",
        "input": event,
    }

    if "body" in event:
        #format an item
        item_json = json.loads(event['body'])
        pk_value = item_json.get(PK)
        sk_value = item_json.get(SK)
        new_value = item_json.get('format')
        if pk_value and sk_value and new_value:
            result = db.MyDb(TABLE_NAME).update_item(\
                pk_value, sk_value, new_value)
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
