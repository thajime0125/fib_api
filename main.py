from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

app = FastAPI()

def fibonacci(n):
    if n < 1:
        return bad_request()
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        an_1 = 1
        an_2 = 1
        for i in range(2, n):
            fib = an_1 + an_2
            an_1 = an_2
            an_2 = fib
        return fib

def bad_request():
    content = {"status": 400, "massage": "Bad Request"}
    return JSONResponse(status_code=400, content=content)

@app.get("/fib")
def get_fibonacci(n: int = Query(...)):
    return {"result": fibonacci(n)}
