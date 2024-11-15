# import yfinance as yf
import finnhub
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

FINNHUB_KEY = os.environ.get("FINNHUB_KEY")
print(FINNHUB_KEY)

# Setup client
finnhub_client = finnhub.Client(api_key=FINNHUB_KEY)


