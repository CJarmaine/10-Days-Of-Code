## functions
## Addition
def add_numbers(n1,n2):
    return n1+n2
def sub_numbers(n1,n2):
    return n1-n2
def mult_numbers(n1,n2):
    return n1*n2
def div_numbers(n1,n2):
    return n1/n2
def pow_numbers(n1,n2):
    return n1**n2
def parse_input(input_str, last_ans):
    parts = input_str.split()
    if len(parts) != 3:
        raise ValueError("Format must be: number operator number")
    
    n1_str, func, n2_str = parts
    func = func.lower()
    n1_str = n1_str.lower()
    n2_str = n2_str.lower()

    if n1_str == "ans":
        n1 = last_ans
    else:
        n1 = float(n1_str)

    if n2_str == "ans":
        n2 = last_ans
    else:
        n2 = float(n2_str)
    
    return n1, func, n2
            

def calculate(n1, func, n2):
    if func in ['+', 'plus']:
        return add_numbers(n1,n2)
    elif func in ['-', 'minus']:
        return sub_numbers(n1,n2)
    elif func in ['*', 'x','multiply']:
        return mult_numbers(n1,n2)
    elif func in ['/', 'divide']:
        if n2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return div_numbers(n1,n2)
    elif func in ['^', 'power','**']:
        return pow_numbers(n1,n2)
    else:
        raise ValueError("Unknown operator")

def normalize_input(input_str):
    for op in ["+", "-", "*", "/", "^"]:
        input_str = input_str.replace(op, f" {op} ")
    return " ".join(input_str.split())

def main():
    last_ans = 0.0
    history = []

    print("Simple Python Calculator")
    print("Type 'help' for instructions, 'history' for previous calculations, 'quit' to exit.")

    while True:
    ## Input function - Asks user question - Splits awnser into 3 bits n1, func, n2
        input_str = input("Hello, What would you like me to calculate? \n").strip()

        if input_str.lower() in ("quit", "exit"):
            break

        if input_str == "":
            continue

        if input_str.lower() == "help":
            print("HELP MENU")
            print("Format: number operator number")
            print("Examples: 1 + 2, 7 ** 6, ans *5")
            print("Operators: + - * or x / ^ or **")
            print("Keywords: ans, help, quit/exit")
            continue

        if input_str.lower() == "history":
            if not history:
                print("No calculations yet.")
            else:
                for i, item in enumerate(history, start=1):
                    print(f"{i}: {item}")
            continue
        
        raw_input = input_str
        input_str = normalize_input(input_str)

        try:
            n1, func, n2 = parse_input(input_str, last_ans)
            ans = calculate(n1, func, n2)
        except ZeroDivisionError as e:
            print(e)
            continue
        except ValueError as e:
            print(e)
            print("Please use format, number operator number (e.g. 1 + 3)")
            continue

        last_ans = ans

        if ans.is_integer():
            print(int(ans))
        else:
            print(ans)

        history.append(f"{raw_input} = {ans}")
if __name__ == "__main__":
    main()