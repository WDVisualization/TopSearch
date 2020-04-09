from django.db import models
from mongoengine import connect, Document, ObjectIdField, BooleanField, LongField, ListField, StringField, EmbeddedDocumentField, EmbeddedDocument

# connect('hotwords_spider',
#         username='fetcher',
#         password='iamnotfetcher',
#         host='47.106.132.194',
#         port=27017,
#         authentication_source='hotwords_spider')


# Create your models here.
class Hotword(EmbeddedDocument):
    key = StringField()
    num = StringField()
    isHot = BooleanField(required=False)
    isNew = BooleanField(required=False)


class Hotwords(Document):
    _id = ObjectIdField()
    updateTime = LongField()
    source = StringField()
    data = ListField(EmbeddedDocumentField(Hotword))
    meta = {'collection': 'hotwords'}
