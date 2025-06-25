FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temperature = int(input('Enter the temperature to convert:'))

option = input('Is this temperature in Celcius or Fahrenheit?(C/F):')

match option:
    case 'C':
        def convert_to_celsius():
            celsius_value = ((temperature-32) / (FAHRENHEIT_TO_CELSIUS_FACTOR ))
            
            return print(f"{temperature}\N{DEGREE SIGN}F is {celsius_value}\N{DEGREE SIGN}C")
        convert_to_celsius()
    case 'F':
        def convert_to_fahreinheit():
            fahrenheit_value = ((temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 )
             
            return print(f"{temperature}\N{DEGREE SIGN}C is {fahrenheit_value}\N{DEGREE SIGN}F")
        convert_to_fahreinheit()
         
    case _:
        print('Invalid option')