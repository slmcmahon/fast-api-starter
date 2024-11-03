from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_version():
    return {"version": "0.1.1"}
