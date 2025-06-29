import tkinter as tk
from tkinter import ttk
import argparse


def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"


class FuturisticCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Futuristic Calculator")
        self.configure(bg="#1e1e1e")
        self.expression = ""
        self._build_ui()

    def _build_ui(self):
        style = ttk.Style()
        style.theme_use("alt")
        style.configure("TButton",
                        foreground="#ffffff",
                        background="#333333",
                        font=("Segoe UI", 12),
                        padding=10)
        style.map("TButton",
                  background=[('active', '#005f5f')])
        self.display = ttk.Entry(self, font=("Segoe UI", 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        for (text, row, column) in buttons:
            action = lambda x=text: self._on_button_click(x)
            ttk.Button(self, text=text, command=action).grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
        for i in range(4):
            self.columnconfigure(i, weight=1)
        for i in range(5):
            self.rowconfigure(i, weight=1)

    def _on_button_click(self, char: str):
        if char == '=':
            self.expression = calculate(self.expression)
        else:
            self.expression += char
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


def main():
    parser = argparse.ArgumentParser(description="Futuristic Calculator")
    parser.add_argument('--test', action='store_true', help='run a simple self-test')
    args = parser.parse_args()
    if args.test:
        print('1+1=', calculate('1+1'))
        print('2*3=', calculate('2*3'))
        print('5/0=', calculate('5/0'))
    else:
        app = FuturisticCalculator()
        app.mainloop()


if __name__ == '__main__':
    main()
