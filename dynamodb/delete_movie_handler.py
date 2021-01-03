import json
import dynamodb.dynamodb as db
from dynamodb.constants import TABLE_NAME, PK, SK

def delete(event, context):
    print(event)

    if "queryStringParameters" in event:
        #get an item
        pk_value = event["queryStringParameters"].get(PK)
        sk_value = event["queryStringParameters"].get(SK)
        if pk_value and sk_value:
            result = db.MyDb(TABLE_NAME).delete_item(pk_value, sk_value)
            print(result)
            response = {
                "statusCode": 200,
                'body': json.dumps(result)
            }
            return response

    body = {
        "message": "DELETE! No return!",
        "input": event,
    }
    response = {
        "statusCode": 500,
        "body": json.dumps(body)
    }

    return response

