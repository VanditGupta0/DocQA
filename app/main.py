from fastapi import FastAPI
app=FastAPI()
@app.get("/health")
def create_app():
    return {"status":"ok"}
@app.get("/greet/{name}")
def greet_user(name:str,shout:bool=False):
    if shout:
        return {"message": f"HELLO, {name.upper()}" }
    else:
        return {"message":f"Hello, {name}!"}