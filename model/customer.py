from model.basemodel import *
from decorators.timeItDecorator import *


@measure_all_class_methods
class Customer(BaseModel):
    __table__ = 'Customer'
    __primary_key__ = 'CustomerId'
    __timestamps__ = False
