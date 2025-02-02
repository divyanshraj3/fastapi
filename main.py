from fastapi import FastAPI
from fastapi.param_functions import Body
app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"data": "post"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}
