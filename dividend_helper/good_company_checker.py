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
    ticker = yf.Ticker(symbol)
    
       # Check if dividends exist
    dividends = ticker.dividends
    if dividends.empty:
        print("There are no Dividend for this stock")

   
    else:
        # Try to get forward dividend yield & ex-dividend date from info
        info = ticker.info
        
        #print(info)

        forward_yield = info.get("dividendYield", None)
        ex_div_date = info.get("exDividendDate", None)  # timestamp (seconds)
        div_yield = info.get("dividendYield",None)
        volume = info.get("volume",None)
        avg_price = info.get("regularMarketPrice", None)
        dividend = avg_price * (div_yield / 100)

        print(f"Symbol: {symbol}")
        print(f"Average Price: {avg_price}")
        print(f"Volume: {volume}")
        print(f"Has Divdends: yes ")
        print(f"Dividend Yield: {div_yield}% ")
        print(f"Dividend: ${dividend:.2f}")

    

    


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


def div_and_apy_compare(money, dividend):
    apy = money *  .04
    print(f"apy = {apy}")
    print(f"dividend = {dividend}")



def ticker_info(symbol):
    yf.Ticker(symbol)

if __name__ == "__main__": 
    stocks = ["AAPL", "SPY", "TSLA", "MSFT", "AMZN",] 
    #new_checker()
    #monthly_data_checker()
    #rsi_indicator("AAPL")
    #print(dividend_details("AAPL"))
    div_and_apy_compare(100000, 456)
   





