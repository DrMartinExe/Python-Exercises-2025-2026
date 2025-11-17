# ==========================================================
# Combined Exercises – Weeks 2 & 4 (Solutions)
# ==========================================================


# ----------------------------------------------------------
# Question 1 – Data Structures: Student Attendance
# ----------------------------------------------------------

monthly_attendance = [92, 88, 85, 90, 94, 89, 91, 93, 87, 95, 90, 92]

# 1. Convert percentages to decimals using list comprehension
attendance_decimals = [a / 100 for a in monthly_attendance]
print("Attendance in decimal form:", attendance_decimals)

# 2. Slice to extract Term 2 (March–June)
term2_attendance = monthly_attendance[2:6]
print("Term 2 attendance (Mar–Jun):", term2_attendance)

# 3. Calculate month-to-month changes
attendance_changes = []
for i in range(1, len(monthly_attendance)):
    change = monthly_attendance[i] - monthly_attendance[i - 1]
    attendance_changes.append(change)
print("Month-to-month changes:", attendance_changes)

# 4. Convert list to tuple (immutable)
attendance_tuple = tuple(monthly_attendance)
print("Attendance tuple:", attendance_tuple)
print("Tuples are used when data should not be accidentally changed, "
      "making them ideal for storing confirmed or historical records.")

# 5. Conditional average check
average_attendance = sum(monthly_attendance) / len(monthly_attendance)
if average_attendance > 90:
    print(f"Average attendance {average_attendance:.1f}% → Excellent overall attendance!")
else:
    print(f"Average attendance {average_attendance:.1f}% → Some improvement needed.")


# ----------------------------------------------------------
# Question 2 – Control Flow & Dictionaries: Fitness Tracker
# ----------------------------------------------------------

weekly_steps = {
    "Alice": [7800, 8450, 9100, 10000],
    "Ben": [5600, 6000, 6200, 7000],
    "Cara": [9800, 10200, 11000, 11500]
}

while True:
    name = input("\nEnter a user name (or 'quit' to exit): ").capitalize()

    if name.lower() == "quit":
        print("Exiting fitness tracker.")
        break

    if name in weekly_steps:
        steps = weekly_steps[name]
        average_steps = sum(steps) / len(steps)
        print(f"{name}'s average weekly steps: {average_steps:.0f}")

        if average_steps >= 9000:
            print("Excellent!")
        elif 7000 <= average_steps < 9000:
            print("Good effort!")
        else:
            print("Needs improvement.")
    else:
        print("User not found.")
