import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.expression = ""
        self.input_text = tk.StringVar()

        # Creating the display frame
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(expand=True, fill='both')

        # Creating the input field inside the display frame
        self.input_field = tk.Entry(self.display_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=30, insertwidth=4, width=14, justify='right')
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(expand=True, fill='both')

        # Creating the buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(expand=True, fill='both')

        # Defining the button layout
        self.buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            'C', '0', '=', '+'
        ]

        row = 0
        col = 0
        for button in self.buttons:
            self.create_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def create_button(self, button, row, col):
        if button == 'C':
            btn = tk.Button(self.buttons_frame, text=button, font=('arial', 18, 'bold'), bd=1, relief='ridge', command=self.clear_input)
        elif button == '=':
            btn = tk.Button(self.buttons_frame, text=button, font=('arial', 18, 'bold'), bd=1, relief='ridge', command=self.evaluate_input)
        else:
            btn = tk.Button(self.buttons_frame, text=button, font=('arial', 18, 'bold'), bd=1, relief='ridge', command=lambda b=button: self.update_input(b))

        btn.grid(row=row, column=col, sticky='nsew')
        self.buttons_frame.grid_rowconfigure(row, weight=1)
        self.buttons_frame.grid_columnconfigure(col, weight=1)

    def update_input(self, value):
        self.expression += value
        self.input_text.set(self.expression)

    def clear_input(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate_input(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
