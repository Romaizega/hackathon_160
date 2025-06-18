from dotenv import load_dotenv
import os
import requests

load_dotenv()
MONEY_KEY = os.getenv("MONEY_KEY")

currency = [
    ("USD", "ILS"),
    ("EUR", "ILS"),
    ("ILS", "USD"),
    ("ILS", "EUR")
]

def get_money():
    for base, target in currency:
        url = f"https://v6.exchangerate-api.com/v6/{MONEY_KEY}/latest/{base}"
        try:
            res = requests.get(url)
            data = res.json()
            if data["result"] == "success":
                rate = data["conversion_rates"].get(target)
                if rate:
                    print(f" 1 {base} = {round(rate, 3)} {target}")
                else:
                    print("Error")
        except ValueError:
            print("Bad request")
