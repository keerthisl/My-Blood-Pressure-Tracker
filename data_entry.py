# data_entry.py
from datetime import datetime

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if not date_str and allow_default:
        return datetime.today().strftime("%d-%m-%Y")
    try:
        date = datetime.strptime(date_str, "%d-%m-%Y")
        return date.strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")
        return get_date(prompt, allow_default)

def get_pressure_reading(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Value must be positive.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_description():
    return input("Enter a description for the reading: ")

def process_data(data_str):
    try:
        date, systolic, diastolic, heart_rate, description = data_str.split('/')
        return {
            "date": [date.strip()],
            "systolic": [int(systolic.strip())],
            "diastolic": [int(diastolic.strip())],
            "heart_rate": [int(heart_rate.strip())],
            "description": [description.strip()],
        }
    except ValueError:
        raise ValueError("Incorrect data format. Please use date/systolic/diastolic/heart_rate/description format.")
