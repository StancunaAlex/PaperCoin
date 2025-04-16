import requests

def fetchPrice():
    try:
        response = requests.get("http://127.0.0.1:5000/btc-price")
        data = response.json()
        return data["price"]
    except Exception as e:
        print(f"Error: {e}")
        return "Error"
