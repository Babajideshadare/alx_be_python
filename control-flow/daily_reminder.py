# daily_reminder.py

task = input("Enter your task: ").strip()

while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ["high", "medium", "low"]:
        break
    print("Please enter a valid priority (high, medium, or low).")

time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

match priority:
    case "high":
        reminder = f"Reminder about the {task}: Hi, do not forget that '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder about the {task}: This '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder about the {task} : Relax, this '{task}' is a low priority task"
    case _:
        reminder = f"Reminder about the {task}e: '{task}' has an unspecified priority level"

if time_bound == "yes":
    reminder += " that requires immediate attention based on tme sensitivity!"
else:
    reminder += ". Consider completing it when you have free time."

print()
print(reminder)





