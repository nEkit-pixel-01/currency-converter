import requests

def get_rate(from_currency, to_currency):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
    data = response.json()
    return data["rates"][to_currency]

def convert(amount, from_currency, to_currency):
    if not isinstance(amount, (int, float)):
        print("Ошибка: введите число")
        return None
    rate = get_rate(from_currency, to_currency)
    result = amount * rate
    return round(result, 2)

def list_currencies():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    return sorted(data["rates"].keys())

if __name__ == "__main__":
    print("Доступные валюты:", list_currencies())
    amount = float(input("Введите сумму: "))
    from_curr = input("Из какой валюты: ").upper()
    to_curr = input("В какую валюту: ").upper()
    result = convert(amount, from_curr, to_curr)
    print(f"Результат: {result}")