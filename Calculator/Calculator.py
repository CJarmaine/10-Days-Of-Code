## Input function - Asks user question - Splits awnser into 3 bits n1, func, n2
input_str = input("Hello, What would you like me to calculate? ").split()

while input_str != "quit":
    n1 = float(input_str[0])
    func = input_str[1]
    n2 = float(input_str[2])
 
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

    if func in ['+', 'plus']:
        ans = add_numbers(n1,n2)
    elif func in ['-', 'minus']:
        ans = sub_numbers(n1,n2)
    elif func in ['*', 'multiply']:
        ans = mult_numbers(n1,n2)
    elif func in ['/', 'divide']:
        if n2 == 0:
            ans = 0
        else:
            ans = div_numbers(n1,n2)
    else:
        print("Error")

    if ans.is_integer():
        print(int(ans))
    else:
        print(ans)
    input_str = input("Hello, What would you like me to calculate? ").split()
