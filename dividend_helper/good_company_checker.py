import yfinance as yf
from termcolor import cprint






def  new_checker():
    # for the news checking function I want to find use a ai to check if the new for the stock is good or not that will help me see if it going to be bad
    # a ticker is a stock  symbol
    # uses the stocks array to check all the news information for each individual stock

    for stock in stocks:
        news = (yf.Ticker(stock).news)
        cprint(f'CURRNET NEWS ON STOCK {stock}', "white","on_yellow")
        for article in news:
            try:
                title = article["content"]["title"]
                summary = article["content"]["summary"]
                link = article["content"]["clickThroughUrl"]["url"]
            
            # type erro is for when there is no link 
            except TypeError as e:
             
                # if there is an error print the error and the article that caused the error
                link = "N/A"
            #color coated the diffrent type of stocks and the terminal
            cprint(f"{stock}'s News ({title})", "black", "on_magenta")
            cprint("Summary: ", "black","on_light_blue", end="")
            cprint(f"{summary}", "blue", "on_white")
            cprint("Link: ", "black","on_light_green", end="")
            cprint(f"{link}", "light_green", "on_white")
        



# for this, this is for
def monthly_data_checker():
    yf.Ticker("AAPL")
    data = yf.download("AAPL", period="1y", interval="1d")
    print(data.head())


def dividend_details(symbol):
    ticker = yf.Ticker("AAPL")
       # Check if dividends exist
    dividends = ticker.dividends
    if dividends.empty:
        return {
            "symbol": symbol,
            "has_dividends": False,
            "message": "This stock does not currently pay dividends."
        }

    # Get most recent dividend paid
    last_div = dividends.iloc[-1]

    # Try to get forward dividend yield & ex-dividend date from info
    info = ticker.info
    forward_yield = info.get("dividendYield", None)
    ex_div_date = info.get("exDividendDate", None)  # timestamp (seconds)

    return {
        "symbol": symbol,
        "has_dividends": True,
        "last_dividend": float(last_div),
        "forward_yield": f"{forward_yield * 100:.2f}%" if forward_yield else "N/A",
        "next_ex_dividend_date": ex_div_date if ex_div_date else "N/A"
    }

    print(f"Symbol: {symbol}")
    print(f"Has Divdends: No ")
    print(f"Latest Divdend: ")
    print(f"forward yield")
    print(f"")

    

    


def rsi_indicator(stock):
    timeframe = 14
    data = yf.download("AAPL", period="1y", interval="1d")
  
    print(data["Close"])
    #avg_gain = data["Close"].rolling(window=timeframe).mean()
    #avg_loss = data["Loss"].rolling(window=timeframe).mean()

    #rs = avg_gain / avg_loss
    #rsi = 100 - (100/ (1+rs))
    #print(rsi)




def sma_indicator(stock):
    pass


def quarterly_earnings_checker():
    pass


if __name__ == "__main__": 
    stocks = ["AAPL", "SPY", "TSLA", "MSFT", "AMZN",] 
    #new_checker()
    #monthly_data_checker()
    #rsi_indicator("AAPL")
    print(dividend_details("AAPL"))
   





