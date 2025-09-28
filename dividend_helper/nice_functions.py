import yfinance as yf
from termcolor import cprint
import tkinter as tk





def  news_checker(stocks):
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
        


def stock_news(stock, listbox):
    listbox.delete(0,tk.END)
    news = (yf.Ticker(stock).news)
    # if they entered incorrect ticker
    print(news)
    if news == []:
        listbox.insert(tk.END,"INVALID TICKER PLEASE TRY AGAIN")
    else:
        # display stock information
        listbox.insert(tk.END,f'CURRNET NEWS ON STOCK {stock}')
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
                listbox.insert(tk.END, f"{stock}'s News ({title})")
                listbox.insert(tk.END,f"Summary: {summary}")
                listbox.insert(tk.END,f"Link: {link}")
                listbox.insert(tk.END,"-"*20)
            
            
        


# for this, this is for
def monthly_data_checker():
    yf.Ticker("AAPL")
    data = yf.download("AAPL", period="1y", interval="1d")
    print(data.head())


def dividend_details(entry, listbox):
    listbox.delete(0,tk.END)
    symbol = entry
    ticker = yf.Ticker(symbol)
    
       # Check if dividends exist
    dividends = ticker.dividends
    if dividends.empty:
        print("There are no Dividend for this stockfds")
        listbox.insert(tk.END, "TICKER NOT VALID PLEASE TRY AGAIN")

   
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

   
        listbox.insert(tk.END, f"Symbol: {symbol}")
        listbox.insert(tk.END, f"Average Price: {avg_price}")
        listbox.insert(tk.END, f"Volume: {volume}")
        listbox.insert(tk.END, f"Dividend Yield: {div_yield}% ")
        listbox.insert(tk.END, f"Dividend: ${dividend:.2f}" )
        listbox.insert(tk.END, "Had Dividens: YES")

    

    


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
    #stocks = ["AAPL", "SPY", "TSLA", "MSFT", "AMZN",] 
    #new_checker()
    #monthly_data_checker()
    #rsi_indicator("AAPL")
    #print(dividend_details("AAPL"))
    div_and_apy_compare(100000, 456)
   





