import tkinter as tk
def launch_calculator():
    loading.destroy()
    show_calculator()

def show_calculator():
    class Calculator:
        def _init_(self, root):
            self.root = root
            self.root.title("Calculator")
            self.root.geometry("360x600")  
            self.root.resizable(False, False)
            self.dark_mode = False
            self.buttons = {}  

            self.create_widgets()
            self.bind_keys()

        def create_widgets(self):
            self.entry = tk.Entry(
                self.root,
                font=("Arial", 30),
                bd=10,
                relief=tk.FLAT,
                justify='right',
                bg='white',
                fg='black'
            )
            self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, sticky="nsew", pady=(10, 0), padx=10)

            buttons = [
                ['C', '⌫', '.', '/'],
                ['7', '8', '9', '*'],
                ['4', '5', '6', '-'],
                ['1', '2', '3', '+'],
                ['Dark', '0', '=', '']
            ]

            for i, row in enumerate(buttons):
                for j, char in enumerate(row):
                    if not char:
                        continue
                    btn = tk.Button(
                        self.root,
                        text=char,
                        font=("Arial", 22),
                        relief=tk.RAISED,
                        bd=4,
                        bg="#333",
                        fg="white",
                        activebackground="#666",
                        activeforeground="white",
                        command=lambda ch=char: self.press(ch)
                    )
                    btn.grid(row=i+1, column=j, sticky="nsew", padx=10, pady=10)
                    self.buttons[char] = btn

            for i in range(4):
                self.root.columnconfigure(i, weight=1)
            for i in range(6):
                self.root.rowconfigure(i, weight=1)

        def highlight_button(self, key):
            if key in self.buttons:
                btn = self.buttons[key]
                original_color = btn.cget("bg")
                btn.config(bg="blue")
                self.root.after(200, lambda: btn.config(bg=original_color))

        def press(self, key):
            self.highlight_button(key)
            if key == "=":
                try:
                    result = str(eval(self.entry.get()))
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, result)
                except:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, "Error")
            elif key == "C":
                self.entry.delete(0, tk.END)
            elif key == "⌫":
                current = self.entry.get()
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, current[:-1])
            elif key == "Dark":
                self.toggle_theme()
            else:
                self.entry.insert(tk.END, key)

        def toggle_theme(self):
            self.dark_mode = not self.dark_mode
            bg = "#1e1e1e" if self.dark_mode else "white"
            fg = "white" if self.dark_mode else "black"
            self.entry.config(bg=bg, fg=fg)
            self.root.config(bg="#121212" if self.dark_mode else "SystemButtonFace")

        def bind_keys(self):
            self.root.bind("<Key>", self.key_input)
            self.root.bind("<Return>", lambda event: self.press("="))
            self.root.bind("<BackSpace>", lambda event: self.press("⌫"))
            self.root.bind("<Delete>", lambda event: self.press("C"))

        def key_input(self, event):
            if event.char in "0123456789+-*/.":
                self.press(event.char)

    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
loading = tk.Tk()
loading.title("Loading...")
loading.geometry("360x600")
loading.configure(bg="white")

label = tk.Label(loading, text="Loading Calculator...", font=("Arial", 18), bg="white", fg="black")
label.pack(expand=True)

loading.after(1000, launch_calculator)
loading.mainloop()
