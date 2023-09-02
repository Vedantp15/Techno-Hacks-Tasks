import tkinter as tk
from tkinter import ttk

# Exchange rates (as of September 2021)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.73,
    "JPY": 109.98,
    "AUD": 1.36,
    "IND": 82.72,
}

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("400x300")
        
        self.amount_label = tk.Label(root, text="Enter amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.from_currency_label = tk.Label(root, text="From currency:")
        self.from_currency_label.pack()

        self.from_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()))
        self.from_currency_combobox.pack()

        self.to_currency_label = tk.Label(root, text="To currency:")
        self.to_currency_label.pack()

        self.to_currency_combobox = ttk.Combobox(root, values=list(exchange_rates.keys()))
        self.to_currency_combobox.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_combobox.get()
            to_currency = self.to_currency_combobox.get()

            if from_currency == to_currency:
                converted_amount = amount
            else:
                converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]

            result_text = f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
            self.result_label.config(text=result_text)
        
        except ValueError:
            self.result_label.config(text="Invalid input")

def main():
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
