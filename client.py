import requests

def fetchPrice(coinSymbol):
    try:
        url = f"http://127.0.0.1:5000/price/{coinSymbol}"
        response = requests.get(url)
        data = response.json()
        return data["price"]
    except Exception as e:
        print(f"Error: {e}")
        return "Error"
