from tkinter import *
import math
import yfinance






def main():
    window = Tk()
    window.geometry("300x300")
    window.title("dividend optimization")
    title = Label(window, text="Enter Ticker(Symbol) of the stock that you want")
    title.pack()
    entry = Entry(window)
    entry.pack()
    frame = Frame(window)
    frame.pack()
    enter_button = Button(frame, text="Enter", command=details)
    enter_button.pack(side=LEFT) 
    dividend_button = Button(frame, text="Dividend Optimization", command=details)
    dividend_button.pack(side=RIGHT)
    blank = Label(window, text="this is working")
    blank.pack()

    

    window.mainloop()

def details():
    blank.config(text="this is working")
    


if '__main__' == __name__:
    main()