from datetime import datetime

from umongo import EmbeddedDocument, Document, fields

from smart_design_store.db import instance


@instance.register
class ProductParams(EmbeddedDocument):
    name = fields.StringField(required=True)
    value = fields.StringField(required=True)


@instance.register
class Product(Document):
    ID = fields.IntField(min_value=1, unique=True)
    name = fields.StringField(required=True)
    description = fields.StringField()
    params = fields.ListField(fields.EmbeddedField(ProductParams))
    created_time = fields.DateTimeField(default=datetime.utcnow)
