from flask import Flask, jsonify
import requests

app = Flask(__name__)

coinList = {
    "btc": "bitcoin",
    "eth": "ethereum",
    "sol": "solana"
}

@app.route('/price/<coin>', methods=['GET'])
def get_price(coin):
    if coin not in coinList:
        return jsonify({"error": "Coin not found"}), 400

    coinID = coinList[coin]

    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coinID}&vs_currencies=usd"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        price = data[coinID]["usd"]

        return jsonify({"price": price, "cached": False})

    except Exception as e:
        print(f"Unexpected error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)