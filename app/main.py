from fastapi import FastAPI
app=FastAPI()
@app.get("/health") 
def health():
    return {"status":"ok"}
@app.get("/greet/{name}") #this is the path parameter /{name}
def greet_user(name:str,shout:bool=False): #shout is a query parameter
    if shout:
        return {"message": f"HELLO, {name.upper()}" }
    else:
        return {"message":f"Hello, {name}!"}