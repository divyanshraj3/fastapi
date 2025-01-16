from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def get_posts():
    return {"data": "post"}