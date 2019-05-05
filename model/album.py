from model.basemodel import *


class Album(BaseModel):
    __table__ = 'Album'
    __primary_key__ = 'AlbumId'
    __timestamps__ = False
