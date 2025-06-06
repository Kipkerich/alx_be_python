num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation= input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
        
    case "-":
        result = num2 - num1
        
    case "*":
        result = num1 * num2
        
    case '/':
        if num2 == 0:
            print('Number cannot be divided by zero')
        else:
            num1/ num2
    case _:
        print("No such operation")
        
print (f'The result is {result}.')