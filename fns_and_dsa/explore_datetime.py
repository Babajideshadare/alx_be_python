# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    current_date = now.date()
    print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date(number_of_days: int):
    current_date = datetime.now().date()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)