import json
import dynamodb.dynamodb as db
from dynamodb.constants import TABLE_NAME, PK, SK

def post(event, context):
    print(event)
    body = {
        "message": "POST! No return!",
        "input": event,
    }

    if "body" in event:
        #format an item
        item_json = json.loads(event['body'])
        if PK in item_json and SK in item_json:
            result = db.MyDb(TABLE_NAME).insert_item(item_json)
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
