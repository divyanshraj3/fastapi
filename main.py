from fastapi import FastAPI
from fastapi.param_functions import Body
from pydantic import BaseModel




app = FastAPI()

class post(BaseModel):      #pydantic to validate the JSON payload from RAW body yady
    title: str
    content: str


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"data": "post"}

@app.post("/createposts")
def create_posts(new_post: post): #taken from the base class
    print(new_post.title)   #just the title for content do new_post.content
    return {"data": "post"}                    # unvalidated request {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}

#validating title str, content str
