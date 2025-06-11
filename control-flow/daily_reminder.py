Task = input("Enter your task:")
Priority =input("Priority (high/medium/low):")
time_bound =input("Is it time-bound? (yes/no)")



match Priority:
    case 'high':
        if time_bound == 'yes':
            print(f" {Task} is a {Priority} priority that requires immediate attention  today!")
        
        else:
            print(f"{Task} is a {Priority} priority task. Consider completing it when you have free time.")
            
    case 'medium':
        if time_bound == 'yes':
                 print(f" {Task} is a {Priority} priority that requires immediate attention  today!")
        
        else:
            print(f"{Task} is a {Priority} priority task. Consider completing it when you have free time.")
            
    case 'low':
        if time_bound == 'yes':
             print(f" {Task} is a {Priority} priority that requires immediate attention  today!")
        
        else:
            print(f"{Task} is a {Priority} priority task. Consider completing it when you have free time.")
            
    case _:
        print('Invalid task input')
            