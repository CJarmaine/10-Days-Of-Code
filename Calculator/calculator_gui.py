import tkinter as tk
from Calculator import normalize_input, parse_input, calculate

display = None

def on_button_click(char):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + char)
    pass

def on_equals():
    expr = display.get()
    try:
        normalized = normalize_input(expr)
        n1, func, n2 = parse_input(normalized, last_ans=0.0)
        ans = calculate(n1,func, n2)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        return
    display.delete(0, tk.END)
    display.insert(0, str(int(ans) if ans.is_integer() else ans))

def main():
    global display
    root = tk.Tk()
    root.title("Calculator")

    display = tk.Entry(root, width=20, font=("Arial", 18), justify="right")
    display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    btn_1 = tk.Button(root, text="1", width=5, height=2, command=lambda: on_button_click("1"))
    btn_1.grid(row=1, column=0, padx=2, pady=2)
    btn_plus = tk.Button(root, text="+", width=5, height=2, command=lambda: on_button_click("+"))
    btn_plus.grid(row=4, column=4, padx=2, pady=2)
    btn_eq = tk.Button(root, text="=", width=5, height=2, command=on_equals)
    btn_eq.grid(row=4, column=3, padx=2, pady=2)
    

    root.mainloop()

if __name__ == "__main__":
    main()