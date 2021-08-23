import json

def get_joke_layer(event, context):
    print("***** Event ****")
    print(event)
    body = {
        "message": "Greetings from Githun. Your function is deployed by a Github Actions. Enjoy your joke",
        "joke":event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

