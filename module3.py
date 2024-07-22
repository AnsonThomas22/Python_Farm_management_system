from datetime import datetime, timedelta

timeindays = {'corn': 365, 'chilli': 186, 'beans': 340, 'carrot': 600}
watering_interval = {'corn': 9, 'chilli': 7, 'beans': 3, 'carrot': 10}
def timeofyield(name):
    time1 = datetime.now()
    
    if name in timeindays:
        days_difference = timeindays[name]
        present_date = time1 + timedelta(days=days_difference)
        print(f"The time for the yield from the present day is {present_date}")

    else:
        print("Name not found in dictionary")
        
def calculate_crop_age(planting_date):
    current_date = datetime.now()
    age = (current_date - planting_date).days
    print(f"The crop is {age} days old.")

def check_watering_time(last_watered_date,name):
    current_date = datetime.now()
    if name in watering_interval:
        watering_interval1= watering_interval[name]
        next_watering_date = last_watered_date + timedelta(days=watering_interval1)
        
    else:
        print("Name not found in dictionary")
    
    if current_date >= next_watering_date:
        print('It is time to water')
    else:
        print('It is not time to water')





