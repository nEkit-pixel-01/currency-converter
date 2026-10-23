from fastapi import FastAPI
from converter import convert, list_currencies
from db import save_conversion, get_history      # 1. новый импорт

app = FastAPI()

@app.get("/convert")
def convert_endpoint(amount: float, from_currency: str, to_currency: str):
    result = convert(amount, from_currency, to_currency)
    save_conversion(from_currency, to_currency, amount, result)   # 2. сохраняем после расчёта
    return {"result": result}

@app.get("/currencies")
def currencies_endpoint():
    return {"currencies": list_currencies()}

@app.get("/history")                              # 3. новый эндпоинт
def history_endpoint(limit: int = 10):
    return {"history": get_history(limit)}
