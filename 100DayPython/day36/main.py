STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "JWC7AWHDIH5VSB90"
TIME_SERIES = "TIME_SERIES_DAILY"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function={TIME_SERIES}&symbol={STOCK_NAME}&apikey={API_KEY}'
response = requests.get(url)
data = response.json()
data_list = [value for (key, value) in data["Time Series (Daily)"].items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data['4. close'])



#TODO 2. - Get the day before yesterday's closing stock price

before_yesterday_data = data_list[1]
before_yesterday_closing_price = float(before_yesterday_data['4. close'])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference_close_price = round(abs(yesterday_closing_price - before_yesterday_closing_price), 2)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

bigger = 0

if before_yesterday_closing_price > yesterday_closing_price:
    bigger = before_yesterday_closing_price
else:
    bigger = yesterday_closing_price

percentage = round(difference_close_price * 100 / bigger, 2)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if(percentage > 5):
    paramsNews5 = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "apiKey": "3dfd6a04d4d54bc7acd754db7fe67543",
        "pageSize": 3
    }
    responseNews5 = requests.get('https://newsapi.org/v2/everything', paramsNews5)
    articles6 = [article for article in responseNews5.json()["articles"]]


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

paramsNews6 = {
    "q": COMPANY_NAME,
    "apiKey": "3dfd6a04d4d54bc7acd754db7fe67543",
}
responseNews6 = requests.get('https://newsapi.org/v2/everything', paramsNews6)
articles6 = [article for article in responseNews6.json()["articles"]]


#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.
slice_articles = articles6[:3]
print(slice_articles)

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

