from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange




app = FastAPI()

class post(BaseModel):      #pydantic to validate the JSON payload from RAW body yady
    title: str
    content: str
    published: bool = True # optional values
    rating: Optional[int] = None    

my_posts = [{'title': 'title of post 1', 'content': 'content of post1', 'id': 1}]


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"data": "post"}

@app.post("/createposts")
def create_posts(posts: post):
    post_dict = posts.dict()
    post_dict['id'] = randrange(0, 1000)
    my_posts.append(post_dict)
                                                                        
    return {"data": post_dict}                    # unvalidated request {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}

#validating title str, content str
