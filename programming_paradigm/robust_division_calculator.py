def safe_divide(numerator, denominator):

   
    try:
      
        result = float(numerator) / float(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        
    except ZeroDivisionError:
        return print('Error: Cannot divide by zero.')
        
    except ValueError:
        return print('Error: Please enter numeric values only.')
        
    else:
         print(f"The result of the division is {result}")
        


safe_divide(12, 2)