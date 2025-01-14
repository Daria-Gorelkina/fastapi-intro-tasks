from fastapi import FastAPI

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/reverse/{text}")
async def func(text: str):
    return {"reversed": text[::-1]}
# END
