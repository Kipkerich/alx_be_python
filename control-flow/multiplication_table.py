number = input('Enter a number to see its multiplication table:')


for mutiple in range(1, 10):
    
    product = number * mutiple
    print(f"{number} * {mutiple} = {product}")
    mutiple = mutiple + 1