import tkinter as tk
import nice_functions

def open_dividend_interface():
    query = entry.get().strip() # get user input and remove extra spaces
    if not query: # if input is empty
        
        return
    
    # new window
    new_win = tk.Toplevel(root)
    new_win.title("Dividend Page")
    new_win.geometry("300x200")

    # show input txt in new window
    label = tk.Label(new_win, text=f"Searching for: {query}", font=("times new roman", 12))
    label.pack(pady=20)

def open_calculate_page():
    # new window for Calculate
    new_win = tk.Toplevel(root)
    new_win.title("Calculate Page")
    new_win.geometry("360x260")

    # Instruction
    instr = tk.Label(new_win, text="Enter values to compare 4% APY vs annual dividend", font=("times new roman", 10))
    instr.pack(pady=(10, 5))

    # Investment amount
    invest_frame = tk.Frame(new_win)
    invest_frame.pack(pady=(5, 2))
    invest_label = tk.Label(invest_frame, text="Investment amount ($):", font=("times new roman", 11))
    invest_label.pack(side=tk.LEFT)
    invest_entry = tk.Entry(invest_frame, width=15, font=("times new roman", 11))
    invest_entry.pack(side=tk.LEFT, padx=6)

    # Annual dividend amount
    div_frame = tk.Frame(new_win)
    div_frame.pack(pady=(5, 8))
    div_label = tk.Label(div_frame, text="Annual dividend ($):", font=("times new roman", 11))
    div_label.pack(side=tk.LEFT)
    div_entry = tk.Entry(div_frame, width=15, font=("times new roman", 11))
    div_entry.pack(side=tk.LEFT, padx=6)

    # Result area
    result_label = tk.Label(new_win, text="", font=("times new roman", 11), fg="blue")
    result_label.pack(pady=(6, 6))

    error_label = tk.Label(new_win, text="", font=("times new roman", 10), fg="red")
    error_label.pack()

    def do_calculate(event=None):
        error_label.config(text="")
        result_label.config(text="")

        # parse inputs
        try:
            invest = float(invest_entry.get().strip())
        except Exception:
            error_label.config(text="Invalid investment amount. Enter a number like 10000")
            return

        try:
            annual_div = float(div_entry.get().strip())
        except Exception:
            error_label.config(text="Invalid dividend amount. Enter a number like 450")
            return

        # compute 4% APY on the investment and compare
        apy_amount = invest * 0.04
        diff = annual_div - apy_amount

        result_text = (f"4% APY on ${invest:,.2f} = ${apy_amount:,.2f}\n"
                       f"Annual dividend = ${annual_div:,.2f}\n"
                       f"Difference (dividend - APY) = ${diff:,.2f}")
        result_label.config(text=result_text)

        # Also push to main listbox for history/visibility
        listbox.insert(tk.END, "CALCULATE: " + f"Invest ${invest:,.2f}, APY ${apy_amount:,.2f}, Div ${annual_div:,.2f}, Diff ${diff:,.2f}")

        # Optionally call helper function to keep existing behavior (prints to console)
        try:
            nice_functions.div_and_apy_compare(invest, annual_div)
        except Exception:
            # ignore errors from helper; GUI result is primary
            pass

    # Buttons
    btn_frame = tk.Frame(new_win)
    btn_frame.pack(pady=(6, 10))
    calc_btn = tk.Button(btn_frame, text="Compare", font=("times new roman", 12), command=do_calculate)
    calc_btn.pack(side=tk.LEFT, padx=8)
    close_btn = tk.Button(btn_frame, text="Close", font=("times new roman", 12), command=new_win.destroy)
    close_btn.pack(side=tk.LEFT, padx=8)

    # Bind Enter on either entry to run the calculation
    invest_entry.bind("<Return>", do_calculate)
    div_entry.bind("<Return>", do_calculate)

root = tk.Tk()
root.title("Search Bar")
root.geometry("400x300")

# --- Search Bar (entry +button)) ---
# --- Search Bar (entry + Dividend button) ---
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

entry = tk.Entry(search_frame, width=30, font=("times new roman", 12))
entry.pack(side=tk.LEFT, padx=5)

dividend_button = tk.Button(search_frame, text="Dividend", font=("times new roman", 12), command=lambda:nice_functions.dividend_details(entry.get(), listbox))
dividend_button.pack(side=tk.LEFT, padx=5)

# --- Second row: News + Calculate ---
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

news_button = tk.Button(button_frame, text="News", font=("times new roman", 12), command=lambda: nice_functions.stock_news(entry.get(), listbox))
news_button.pack(side=tk.LEFT, padx=5)

calc_button = tk.Button(button_frame, text="Calculate", font=("times new roman", 12), command=open_calculate_page)
calc_button.pack(side=tk.LEFT, padx=5)




# --- Listbox ---
listbox = tk.Listbox(root, width=40, height=10, font=("times new roman", 12))
listbox.pack(pady=10) #box to display results

status = tk.Label(root, text="Type a query above.", font=("times new roman", 10))
status.pack() # act as status bar


root.mainloop()
