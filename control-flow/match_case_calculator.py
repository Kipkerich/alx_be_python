num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

operation= input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        result = num1 + num2
        print(f'The result is {result}.')  

        
        
    case "-":
        result = num2 - num1
        print(f'The result is {result}.')  

       
    case "*":
        result = num1 * num2
        print(f'The result is {result}.')  

       
    case '/':
        if num2 == 0:
            print('Cannot be divided by zero')
        else:
            result = num1/ num2
            
    case _:
        print("No such operation")
    
 
