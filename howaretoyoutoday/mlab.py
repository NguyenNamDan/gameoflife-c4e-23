import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds151927.mlab.com:51927/howareyoutoday

host = "ds151927.mlab.com"
port = 51927
db_name = "howareyoutoday"
user_name = "admin"
password = "admin1"

#connect data
def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())