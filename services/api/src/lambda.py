from core.schemas.event import Event

def handler(event, context):
    e = Event(id=1, type="user_registered", message="Welcome")
    print(e)
    return {"statusCode": 200, "body": "🌎"}


