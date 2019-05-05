from model.basemodel import *
from decorators.timeItDecorator import *


@measure_all_class_methods
class User(BaseModel):
    __table__ = 'STWUSER'
    __primary_key__ = 'id'
    __timestamps__ = False
