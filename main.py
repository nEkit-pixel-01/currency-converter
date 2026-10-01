from fastapi import FastAPI
from converter import convert, list_currencies

app = FastAPI()

@app.get("/convert")
def convert_endpoint(amount: float, from_currency: str, to_currency: str):
    result = convert(amount, from_currency, to_currency)
    return {"result": result}

@app.get("/currencies")
def currencies_endpoint():
    return {"currencies": list_currencies()}