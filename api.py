from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

# Simple in-memory cache to avoid rate-limiting
cache = {
    "price": None,
    "timestamp": 0
}

CACHE_TIMEOUT = 10  # seconds

@app.route('/btc-price', methods=['GET'])
def get_btc_price():
    current_time = time.time()

    # Use cached value if recent
    if cache["price"] and (current_time - cache["timestamp"]) < CACHE_TIMEOUT:
        return jsonify({"price": cache["price"], "cached": True})

    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        price = data["bitcoin"]["usd"]

        # Update cache
        cache["price"] = price
        cache["timestamp"] = current_time

        return jsonify({"price": price, "cached": False})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
