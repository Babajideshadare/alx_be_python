# daily_reminder.py
task = input("Enter your task: ")   
priority = input("Priority (high/medium/low): ")  
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unspecified priority level"
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time." 
print(reminder)

