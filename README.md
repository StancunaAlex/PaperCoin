# PaperCoin

PaperCoin is a simple Python-based trading app. It allows you to simulate and try out any trading strategies on layer 1 coins. It is part of a small project for learning and developing Python applications.
The app uses Flask, Requests, PyQt6 and SQLite.


## Features

- Fully simulated crypto trading.
- Fetches live price data using CoinGecko's API and caches it.
- Adjustable fees and slippage so you can simulate any situation.
- You can add as much cash to your balance as you want.
- Provides statistics for each coin and the overall statistics.
- Login and register system that allows multiple different accounts stored locally.


## How to install

### Prerequisites

- [Python 3.8 or higher](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Installation

Clone the repo using:
```bash
git clone https://github.com/StancunaAlex/PaperCoin.git
```

Then you need to navigate to the project folder:
```bash
cd PaperCoin
```

After that you need to install the required dependencies:
```bash
pip install -r requirements.txt
```

### Running the app

You can start the application with:
```bash
python -m papercoin
```

## How to use

The app is very simple to use. After opening it, you need to register an account. The account only needs to have a name and a password. After registering, you will be taken to the main screen where you can choose which coin you want to trade and how much do you want to buy or sell.

To add funds to your account, click on **Edit** and then **Add Balance**. In the **Edit** menu you can also select **Fees and Slippage**. This will open up a menu that allows you to change the percentage you will have to pay for in fees or in slippage.

After adding your balance and adjusting the fees and slippage, you are ready to try out your trading strategies. You can view more detailed statistics by clicking the **View** button, and logout via the **Settings** button.

## Contributing

If you find any bugs, feel free to send an email at **alexandrustancuna23@gmail.com**
