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
    new_win.geometry("300x200")

    # Entry box (holder bar)
    calc_entry = tk.Entry(new_win, width=25, font=("times new roman", 12))
    calc_entry.pack(pady=20)

    # Enter button (does nothing yet)
    enter_button = tk.Button(new_win, text="Enter", font=("times new roman", 12))
    enter_button.pack(pady=5)

root = tk.Tk()
root.title("Search Bar")
root.geometry("400x300")

# --- Search Bar (entry +button)) ---
# --- Search Bar (entry + Dividend button) ---
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

entry = tk.Entry(search_frame, width=30, font=("times new roman", 12))
entry.pack(side=tk.LEFT, padx=5)

dividend_button = tk.Button(search_frame, text="Dividend", font=("times new roman", 12), command=open_dividend_interface)
dividend_button.pack(side=tk.LEFT, padx=5)

# --- Second row: News + Calculate ---
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

news_button = tk.Button(button_frame, text="News", font=("times new roman", 12))
news_button.pack(side=tk.LEFT, padx=5)

calc_button = tk.Button(button_frame, text="Calculate", font=("times new roman", 12), command=open_calculate_page)
calc_button.pack(side=tk.LEFT, padx=5)


# --- Listbox ---
listbox = tk.Listbox(root, width=40, height=10, font=("times new roman", 12))
listbox.pack(pady=10) #box to display results

status = tk.Label(root, text="Type a query above.", font=("times new roman", 10))
status.pack() # act as status bar


root.mainloop()
