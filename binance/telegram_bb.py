import telegram
from binance.client import Client
import time

api_key = "mSZp7NPYBy0kq0Bs9CdmbNYmC3TqnAVQCYFqByzcZNZ93LL5mfP3La3Aw8VAevvP"
api_secret = "PtTC9McSur1KfMo8Jn2GRHb9m0zkNIG9WQitXVCBd9MjqDeuMV00vEEhSDYVlZKi"

bot_token = "6090948283:AAGBoE-jzakrcKBtw49_pC7mJebm5OtwP5s"

telegram_group_id = "5204008772"

traders_to_follow = ["FxTrading-pro", "Degen-Ape-Trader", "VB1"]

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