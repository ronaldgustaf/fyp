
from api import finnhub_client
import yfinance as yf
from helpers import get_lookback_date, format_date, DATE_FORMAT
import pandas as pd
from datetime import datetime


# Company Info
def get_company_info(ticker:str, start_date: str, end_date:str, date_format=DATE_FORMAT):
    pass

# News Data
def get_news_data(ticker: str, start_date: str, end_date:str, date_format=DATE_FORMAT):
    start_date = format_date(start_date, current_format=date_format)
    end_date = format_date(end_date, current_format=date_format)
    
                                   
    news_data = finnhub_client.company_news(ticker, _from=start_date, to=end_date)
    news_data = [
        {
            "date": datetime.fromtimestamp(news['datetime']).strftime('%d-%m-%Y'),
            "headline": news['headline'],
            "summary": news['summary'],
        } for news in news_data
    ]
    
    news_data = pd.DataFrame(news_data)

    return news_data

# Fundamentals Data
def get_fundamentals_data(ticker: str, start_date: str, end_date:str):
    pass

# Stock Data
def get_stock_data(ticker, start_date, end_date, date_format=DATE_FORMAT):
    start_date = format_date(start_date, current_format=date_format)
    end_date = format_date(end_date, current_format=date_format)


    stock_data = yf.download(ticker, start=start_date, end=end_date)

    stock_data = stock_data['Adj Close']
    stock_data = stock_data.reset_index()
    stock_data['Date'] = stock_data['Date'].dt.strftime(date_format)
    stock_data = stock_data.rename_axis(None, axis=1)

    return stock_data

# Macro Data
def get_macro_data(ticker: str, start_date: str, end_date:str):
    pass


# Company Info
def get_company_info(ticker:str, start_date: str, end_date:str, date_format=DATE_FORMAT):
    cprof = finnhub_client.company_profile2(symbol='AAPL')
    df = pd.DataFrame(cprof, index=[0])
    df['shareOutstanding']  = df['shareOutstanding'] * 1E6
    df['marketCapitalization'] = df['marketCapitalization'] * 1E6
    
    return df