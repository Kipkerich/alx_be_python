def safe_divide(numerator, denominator):
    numerator = float(input('Value of numerator'))
    denominator= float(input('Value of denominator'))
    try:
        result = numerator / denominator
        if denominator == 0:
            raise ZeroDivisionError
        
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
        
    except ValueError:
        print('Error: Please enter numeric values only')
        
    else:
        print(f"The result of the division is {result}")