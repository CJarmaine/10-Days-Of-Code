## Input function - Asks user question - Splits awnser into 3 bits n1, func, n2
input_str = input("Hello, What would you like me to calculate? ").split()

n1 = int(input_str[0])
func = input_str[1]
n2 =  int(input_str[2])

## functions

if func == '+' or 'plus':
    x = n1 + n2
elif func == '-' or 'minus' :
    x = n1 - n2
elif func == '*' or 'multiply':
    x = n1 * n2
elif func == '/' or 'divide':
    x = n1 / n2
else:
    print("Error")
print(x)