from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

cache = {}

cacheTimeout = 10 

# Add coins and convert them for the url
coinList = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "sol": "solana"
}

@app.route('/price/<coin>', methods=['GET'])
def get_price(coin):

    coinID = coinList[coin]
    cacheTime = time.time()

    # Initialize coin cache if not present
    if coin not in cache:
        cache[coin] = {"price": None, "timestamp": 0}

    # Use cached price
    if cache[coin]["price"] and (cacheTime - cache[coin]["timestamp"]) < cacheTimeout:
        return jsonify({"price": cache[coin]["price"], "cached": True})

    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coinID}&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        price = data[coinID]["usd"]

        # Update cache
        cache[coin]["price"] = price
        cache[coin]["timestamp"] = cacheTime

        return jsonify({"price": price, "cached": False})
    except Exception as e:
        return jsonify({f"error": e}), 500

if __name__ == '__main__':
    app.run(debug=True)
