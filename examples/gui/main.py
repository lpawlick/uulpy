import tkinter as tk
from ttkbootstrap.constants import *

from uulpy import UUL, Currency

def run_clicker():

    def increase_counter():
        uul.tick()
        counter.set(str(uul.currencies.usd))

    root = tk.Tk()
    root.title("Clicker")

    uul = UUL(currencies=[Currency(name="usd", format_str="{amount} {symbol}")])
    counter = tk.StringVar()
    counter.set(str(uul.currencies.usd))

    # Set the window size
    window_width = 1920
    window_height = 1080
    root.geometry(f"{window_width}x{window_height}")

    left_frame = tk.Frame(root, width=window_width // 4)
    right_frame = tk.Frame(root, width=3 * window_width // 4)

    left_frame.grid(row=0, column=0, sticky="nsew")
    right_frame.grid(row=0, column=1, sticky="nsew")

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=3)

    button = tk.Button(left_frame, text="Increase", command=increase_counter, width=left_frame.winfo_reqwidth() // 16, height=left_frame.winfo_reqheight() * 4)
    counter_label = tk.Label(right_frame, textvariable=counter, font=("Arial", 30))

    button.pack(pady=10)
    counter_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_clicker()