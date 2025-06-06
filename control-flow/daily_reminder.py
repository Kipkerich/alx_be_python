task = input("Enter your task:")
task_priority =input("Priority (high/medium/low):")
time_bound =input("Is it time bound? (yes/no)")

match task_priority:
    case 'high':
        if time_bound == 'yes':
            print(f" {task} is a {task_priority} priority that requires immediate attention  today!")
        
        else:
            print(f"{task} is a {task_priority} priority task. Consider completing it when you have free time.")
            
    case 'medium':
        if time_bound == 'yes':
                 print(f" {task} is a {task_priority} priority that requires immediate attention  today!")
        
        else:
            print(f"{task} is a {task_priority} priority task. Consider completing it when you have free time.")
            
    case 'low':
        if time_bound == 'yes':
             print(f" {task} is a {task_priority} priority that requires immediate attention  today!")
        
        else:
            print(f"{task} is a {task_priority} priority task. Consider completing it when you have free time.")
            
    case _:
        print('Invalid task input')
            