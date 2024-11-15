from datetime import datetime, timedelta

DATE_FORMAT = "%d-%m-%Y"

def get_lookback_date(target_date: str, lookback_window: int, date_format=DATE_FORMAT):
    
    date_obj = datetime.strptime(target_date, date_format)
    lookback_date = datetime.strftime(date_obj - timedelta(days=lookback_window - 1), date_format)
    
    return lookback_date

def format_date(str_date: str, current_format=DATE_FORMAT, new_format="%Y-%m-%d"):
    str_date = datetime.strptime(str_date, current_format)
    str_date = datetime.strftime(str_date, new_format)    
    
    return str_date
