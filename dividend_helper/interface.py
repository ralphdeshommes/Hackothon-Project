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


root = tk.Tk()
root.title("Search Bar")
root.geometry("400x300")

# --- Search Bar (entry +button)) ---
search_frame = tk.Frame(root)
search_frame.pack(pady=10) # text field inside frame, adds 10px of vert space

entry = tk.Entry(search_frame, width=30, font=("times new roman", 12))
entry.pack(side=tk.LEFT, padx=5) #place entry on left side

button = tk.Button(search_frame, text="Dividend", font=("times new roman", 12),command=lambda: nice_functions.dividend_details(entry.get(), listbox))
button.pack(side=tk.LEFT, padx=5) # creates seach button, does not do anything yet

# --- Listbox ---
listbox = tk.Listbox(root, width=40, height=10, font=("times new roman", 12))
listbox.pack(pady=10) #box to display results

status = tk.Label(root, text="Type a query above.", font=("times new roman", 10))
status.pack() # act as status bar


root.mainloop()
