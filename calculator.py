import customtkinter as ctk

class Calculator(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculos - Futuristic Calculator")
        self.geometry("300x400")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        self.display = ctk.CTkEntry(self, font=("Segoe UI", 24), justify='right')
        self.display.pack(fill='both', padx=10, pady=10)
        
        btns_frame = ctk.CTkFrame(self)
        btns_frame.pack(expand=True, fill='both')
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, column) in buttons:
            btn = ctk.CTkButton(btns_frame, text=text, command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=column, sticky='nsew', padx=5, pady=5)
        
        for i in range(4):
            btns_frame.columnconfigure(i, weight=1)
            btns_frame.rowconfigure(i+1, weight=1)
        
    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, ctk.END)
                self.display.insert(ctk.END, str(result))
            except Exception:
                self.display.delete(0, ctk.END)
                self.display.insert(ctk.END, "Error")
        else:
            self.display.insert(ctk.END, char)

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()
