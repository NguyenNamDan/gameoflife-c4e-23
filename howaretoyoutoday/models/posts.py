from mongoengine import *

class Post(Document): 
    time = StringField()
    emoji = StringField()
    status = StringField()
    user = ReferenceField("User") #tro toi 1 thang khac (User)


    
