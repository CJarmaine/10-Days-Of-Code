input_str = input("Hello, What would you like me to calculate? ").split()

n1 = int(input_str[0])
func = input_str[1]
n2 =  int(input_str[2])

## functions

if func == '+' :
    x = n1 + n2
else:
    print("Error")
print(x)