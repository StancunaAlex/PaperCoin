from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

# Cache now stores data per coin
cache = {}

CACHE_TIMEOUT = 10  # seconds

# Mapping from coin name to CoinGecko ID
SUPPORTED_COINS = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "sol": "solana"
    # Add more as needed
}

@app.route('/price/<coin>', methods=['GET'])
def get_price(coin):
    coin = coin
    if coin not in SUPPORTED_COINS:
        return jsonify({"error": "Unsupported coin"}), 400

    coin_id = SUPPORTED_COINS[coin]
    current_time = time.time()

    # Initialize coin cache if not present
    if coin not in cache:
        cache[coin] = {"price": None, "timestamp": 0}

    # Return cached value if still valid
    if cache[coin]["price"] and (current_time - cache[coin]["timestamp"]) < CACHE_TIMEOUT:
        return jsonify({"price": cache[coin]["price"], "cached": True})

    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        price = data[coin_id]["usd"]

        # Update cache
        cache[coin]["price"] = price
        cache[coin]["timestamp"] = current_time

        return jsonify({"price": price, "cached": False})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
