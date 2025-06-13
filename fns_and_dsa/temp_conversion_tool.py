FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = int(input('Enter the temperature to convert:'))

option = input('Is this temperature in Celcius or Fahrenheit?(C/F):')

match option:
    case 'C':
        def convert_to_celsius(fahrenheit):
            celsius_value = ((fahrenheit-32) / (FAHRENHEIT_TO_CELCIUS_FACTOR ))
            
            print(f"{temperature}&degF is {celsius_value}&degC")
        
    case 'F':
        def convert_to_fahreinheit(celsius):
            fahrenheit_value = ((celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 )
             
            print(f"{temperature}&degC is {fahrenheit_value}&degF")
         
    case _:
        print('Invalid option')