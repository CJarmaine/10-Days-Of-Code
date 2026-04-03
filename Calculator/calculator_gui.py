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

## Buttons 4 x 3
    btn_1 = tk.Button(root, text="1", width=5, height=2, command=lambda: on_button_click("1"))
    btn_1.grid(row=1, column=0, padx=2, pady=2)
    btn_2 = tk.Button(root, text="2", width=5, height=2, command=lambda: on_button_click("2"))
    btn_2.grid(row=1, column=1, padx=2, pady=2)
    btn_3 = tk.Button(root, text="3", width=5, height=2, command=lambda: on_button_click("3"))
    btn_3.grid(row=1, column=2, padx=2, pady=2)
    btn_4 = tk.Button(root, text="4", width=5, height=2, command=lambda: on_button_click("4"))
    btn_4.grid(row=2, column=0, padx=2, pady=2)
    btn_5 = tk.Button(root, text="5", width=5, height=2, command=lambda: on_button_click("5"))
    btn_5.grid(row=2, column=1, padx=2, pady=2)
    btn_6 = tk.Button(root, text="6", width=5, height=2, command=lambda: on_button_click("6"))
    btn_6.grid(row=2, column=2, padx=2, pady=2)
    btn_7 = tk.Button(root, text="7", width=5, height=2, command=lambda: on_button_click("7"))
    btn_7.grid(row=3, column=0, padx=2, pady=2)
    btn_8 = tk.Button(root, text="8", width=5, height=2, command=lambda: on_button_click("8"))
    btn_8.grid(row=3, column=1, padx=2, pady=2)
    btn_9 = tk.Button(root, text="9", width=5, height=2, command=lambda: on_button_click("9"))
    btn_9.grid(row=3, column=2, padx=2, pady=2)
    btn_0 = tk.Button(root, text="0", width=5, height=2, command=lambda: on_button_click("0"))
    btn_0.grid(row=4, column=1, padx=2, pady=2)

## functions
    btn_plus = tk.Button(root, text="+", width=5, height=2, command=lambda: on_button_click("+"))
    btn_plus.grid(row=1, column=3, padx=2, pady=2)
    btn_minus = tk.Button(root, text="-", width=5, height=2, command=lambda: on_button_click("-"))
    btn_minus.grid(row=2, column=3, padx=2, pady=2)
    btn_eq = tk.Button(root, text="=", width=5, height=2, command=on_equals)
    btn_eq.grid(row=4, column=2, padx=2, pady=2)
    btn_div = tk.Button(root, text="/", width=5, height=2, command=lambda: on_button_click("/"))
    btn_div.grid(row=4, column=3, padx=2, pady=2)
    btn_mult = tk.Button(root, text="*", width=5, height=2,  command=lambda: on_button_click("*"))
    btn_mult.grid(row=3, column=3, padx=2, pady=2)

    btn_ans = tk.Button(root, text="ans", width=5, height=2,  command=lambda: on_button_click("ans"))
    btn_ans.grid(row=4, column=0, padx=2, pady=2)
    

    root.mainloop()

if __name__ == "__main__":
    main()