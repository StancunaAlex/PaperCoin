import requests
import time

cache = {}
CACHE_TIMEOUT = 30 

def fetchPrice(coinSymbol):
    currentTime = time.time()

    if coinSymbol in cache:
        cachedData = cache[coinSymbol]
        if currentTime - cachedData["timestamp"] < CACHE_TIMEOUT:
            print(f"Using cached price for {coinSymbol}")
            return {"price": cachedData["price"], "cached": True}

    try:
        url = f"http://127.0.0.1:5000/price/{coinSymbol}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "price" in data:
            price = data["price"]
            cache[coinSymbol] = {"price": price, "timestamp": currentTime}
            print(f"Fetched new price for {coinSymbol}: {price}")
            return {"price": price, "cached": False}
        else:
            print(f"Error: {data.get('error', 'Unknown error')}")
            return {"error": "Failed to fetch price"}
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {"error": str(e)}