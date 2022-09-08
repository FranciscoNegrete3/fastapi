from typing import List, Union
from pydantic import BaseModel

class PostBase(BaseModel):
    name: str
    year: int
    #description: Union[str, None] = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    raceId : int
    url : str

    class Config:
        orm_mode = True



