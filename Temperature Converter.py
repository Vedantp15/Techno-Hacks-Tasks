import tkinter as tk
from tkinter import ttk

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("400x300")

        self.temperature_label = tk.Label(root, text="Enter temperature:")
        self.temperature_label.pack()

        self.temperature_entry = tk.Entry(root)
        self.temperature_entry.pack()

        self.from_unit_label = tk.Label(root, text="From unit:")
        self.from_unit_label.pack()

        self.from_unit_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit"])
        self.from_unit_combobox.pack()

        self.to_unit_label = tk.Label(root, text="To unit:")
        self.to_unit_label.pack()

        self.to_unit_combobox = ttk.Combobox(root, values=["Celsius", "Fahrenheit"])
        self.to_unit_combobox.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.convert_button = tk.Button(root, text="Convert", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        try:
            temperature = float(self.temperature_entry.get())
            from_unit = self.from_unit_combobox.get()
            to_unit = self.to_unit_combobox.get()

            if from_unit == to_unit:
                converted_temperature = temperature
            elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                converted_temperature = (temperature * 9/5) + 32
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                converted_temperature = (temperature - 32) * 5/9

            result_text = f"{temperature:.2f} {from_unit} = {converted_temperature:.2f} {to_unit}"
            self.result_label.config(text=result_text)

        except ValueError:
            self.result_label.config(text="Invalid input")

def main():
    root = tk.Tk()
    converter = TemperatureConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
