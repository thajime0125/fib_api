from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse

app = FastAPI()

def fibonacci(n):
    if n < 1:
        raise HTTPException(status_code=400)
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

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(content={"status": 400, "message": "Bad request."}, status_code=exc.status_code)

@app.get("/fib")
def get_fibonacci(n: int = Query(...)):
    return {"result": fibonacci(n)}
