# ==========================================================
# Combined Exercises – Weeks 2 & 4
# ==========================================================
# These exercises test your understanding of:
# - Lists, slicing, and list comprehensions
# - Loops and calculations
# - Dictionaries, conditionals, and user input
# ==========================================================


# ----------------------------------------------------------
# Question 1 – Data Structures: Student Attendance
# ----------------------------------------------------------
# You are analysing monthly attendance data (as a percentage)
# for a group of students in one academic year.
#
# monthly_attendance = [92, 88, 85, 90, 94, 89, 91, 93, 87, 95, 90, 92]
#
# 1. Write a list comprehension to convert percentages into decimal
#    form (e.g., 92 → 0.92).
# 2. Slice the list to extract attendance for the second term
#    (March–June).
# 3. Use a loop to calculate and print the change in attendance
#    from one month to the next. Store these in `attendance_changes`.
# 4. Convert the attendance list into a tuple and explain why tuples
#    might be used for storing confirmed historical records.
# 5. (Extension) Use a conditional to print whether the average
#    attendance across the year was above 90%.


# ----------------------------------------------------------
# Question 2 – Control Flow & Dictionaries: Fitness Tracker
# ----------------------------------------------------------
# You are designing a simple fitness tracking program that records
# users’ weekly step counts.
#
# weekly_steps = {
#     "Alice": [7800, 8450, 9100, 10000],
#     "Ben": [5600, 6000, 6200, 7000],
#     "Cara": [9800, 10200, 11000, 11500]
# }
#
# 1. Ask the user to input a name.
# 2. Check if that name exists in the dictionary.
# 3. If it exists:
#       - Use a loop to calculate the average weekly steps.
#       - Print the name and average step count.
#       - Use an if statement to print:
#           "Excellent!" if average ≥ 9000,
#           "Good effort!" if between 7000–8999,
#           or "Needs improvement." if below 7000.
# 4. If the name doesn’t exist, print "User not found."
# 5. (Extension) Use a while loop to allow repeated lookups
#    until the user types "quit".
#
# (Hint: You can use sum() and len() to calculate averages.)
