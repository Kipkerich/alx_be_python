from datetime import datetime, timedelta


def display_current_datetime():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    return print('Current date and time:', formatted_time)

display_current_datetime()


def calculate_future_date():
    
    number_of_days = int(input('Enter the  number of days to add to the current date:'))
    current_time = datetime.now()
    future_date =  current_time.replace(day= current_time.day + number_of_days)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return print('Future date:', formatted_time)

calculate_future_date()