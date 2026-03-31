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
last_ans = 0.0

while True:

## Input function - Asks user question - Splits awnser into 3 bits n1, func, n2
    input_str = input("Hello, What would you like me to calculate? ").strip()

    if input_str.lower() == "quit":
        break
    
    parts = input_str.split()

    if len(parts) != 3:
        print("Please use format, number operator number (e.g. 1 + 3)")
        continue

    n1_str, func, n2_str = parts
    func = func.lower()
    n1_str = n1_str.lower()
    n2_str = n2_str.lower()
    if n1_str == "ans" and n2_str == "ans":
        try:
            n1 = last_ans
            n2 = last_ans
        except ValueError:
            print("Invalid Input")
            continue        
    elif n1_str == "ans":
        try:
            n1 = last_ans
            n2 = float(n2_str)
        except ValueError:
            print("Invalid Input")
            continue        
    elif n2_str == "ans":
        try:
            n1 = float(n1_str)
            n2 = last_ans
        except ValueError:
            print("Invalid Input")
            continue        
        
    else:
        try:
            n1 = float(n1_str)
            n2 = float(n2_str)
        except ValueError:
            print("Invalid Input")
            continue        
        ## n1 = float(input_str[0])
    ## func = input_str[1]
    ## n2 = float(input_str[2])
 
    if func in ['+', 'plus']:
        ans = add_numbers(n1,n2)
    elif func in ['-', 'minus']:
        ans = sub_numbers(n1,n2)
    elif func in ['*', 'x','multiply']:
        ans = mult_numbers(n1,n2)
    elif func in ['/', 'divide']:
        if n2 == 0:
            print("Cannot divide by zero!")
            continue
        ans = div_numbers(n1,n2)
    else:
        print("Error")
        continue

    last_ans = ans

    if ans.is_integer():
        print(int(ans))
    else:
        print(ans)