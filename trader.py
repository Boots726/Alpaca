
import time
import alpaca_trade_api as tradeapi
import numpy as np
from model import LSTMModel
from config import *

class TraderBot:
    def __init__(self):
        self.api = tradeapi.REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, ALPACA_BASE_URL)
        self.model = LSTMModel()
        self.running = True

    def run(self):
        print("Trader running...")
        while self.running:
            try:
                data = self.api.get_barset("AAPL", "15Min", limit=60).df["AAPL"]
                prices = data["close"].values.reshape(-1, 1)
                prediction = self.model.predict(prices)
                decision = self.make_decision(prediction)
                if decision == "buy":
                    self.api.submit_order(symbol="AAPL", qty=1, side="buy", type="market", time_in_force="gtc")
                elif decision == "sell":
                    self.api.submit_order(symbol="AAPL", qty=1, side="sell", type="market", time_in_force="gtc")
                time.sleep(3600)
            except Exception as e:
                print(f"Error in trader: {e}")

    def make_decision(self, prediction):
        if prediction > 0.6:
            return "buy"
        elif prediction < 0.4:
            return "sell"
        else:
            return "hold"

    def stop(self):
        self.running = False
