
task=(input("Enter your task: " ))
priority=(input("Priority (high/medium/low): "))
time_bound=(input("Is id time-bound (yes/no): "))
# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound.lower() == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a high priority task. Make sure to complete it soon!"
    case "medium":
        if time_bound.lower() == "yes":
            reminder = f"'{task}' is a medium priority task that requires attention today!"
        else:
            reminder = f"'{task}' is a medium priority task. Try to complete it soon!"
    case "low":
        if time_bound.lower() == "yes":
            reminder = f"'{task}' is a low priority task, but it needs to be done today!"
        else:
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."

# Provide a Customized Reminder
print("Reminder:", reminder)
 