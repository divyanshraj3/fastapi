from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel
from typing import Optional




app = FastAPI()

class post(BaseModel):      #pydantic to validate the JSON payload from RAW body yady
    title: str
    content: str
    published: bool = True # optional values
    rating: Optional[int] = None    


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"data": "post"}

@app.post("/createposts")
def create_posts(new_post: post):                            #taken from the base class
    print(new_post)
    print(new_post.model_dump())           #a different form of dict?????

                                               
    return {"data": new_post}                    # unvalidated request {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}

#validating title str, content str
