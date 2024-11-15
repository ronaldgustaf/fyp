from data import get_news_data, get_stock_data, get_company_info


def sample_news(news, k=5):
    # TODO add filtering for better news
    
    return news.iloc[:k]

def news_prompt(ticker, lookback_date, target_date):
    news = get_news_data(ticker, lookback_date, target_date)
    sampled_news = sample_news(news)
    prompt = f"""# News Summary\n\n"""
    for i, n in sampled_news.iterrows():
        prompt += f"[Headline] {n['headline']}\n[Summary] {n['summary']}\n\n"
        
    return prompt
