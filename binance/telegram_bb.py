import telegram
from binance.client import Client
import time

api_key = "Enter Your Binance api_key"
api_secret = "Enter your secret api_secret key"

bot_token = "Enter your bot telegram token"

telegram_group_id = "Your telegram bot group id"

traders_to_follow = ["FxTrading-pro", "Degen-Ape-Trader", "VB1"] #<- The top traders you want to follow

client = Client(api_key, api_secret)

bot = telegram.Bot(token=bot_token)

last_trades = {}
for trader in traders_to_follow:
    last_trade = client.futures_account_trades(symbol="", startTime=int(time.time()*1000), endTime=int(time.time()*1000), limit=1)
    if last_trade:
        last_trades[trader] = last_trade[0]["orderId"]

while True:
    for trader in traders_to_follow:
        trades = client.futures_account_trades(symbol="")
        for trade in trades:
            if trade["orderId"] > last_trades[trader]:
                message = f"🚀 Nouveau trade de {trader} sur {trade['symbol']} : {trade['side']} {trade['qty']} contrats à un prix moyen de {trade['price']}. Le levier utilisé est de {trade['leverage']}."
                bot.send_message(chat_id=telegram_group_id, text=message)
                last_trades[trader] = trade["orderId"]
            elif trade["orderId"] == last_trades[trader] and trade["status"] == "FILLED":
                message = f"🛑 {trader} vient de fermer son trade sur {trade['symbol']} : {trade['side']} {trade['qty']} contrats à un prix moyen de {trade['price']}."
                bot.send_message(chat_id=telegram_group_id, text=message)
                last_trades[trader] = trade["orderId"]
    time.sleep(10)
