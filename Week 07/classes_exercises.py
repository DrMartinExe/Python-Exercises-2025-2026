# =========================================
# Week 7 — Introduction to Object-Oriented Programming (OOP)
# Save as exercises7.py
#
# Topics:
#   - Classes and Objects
#   - The __init__() method
#   - Working with attributes and methods
#   - Setting and modifying attribute values
# =========================================

# -------------------------------------------------
# Task A: Creating a Simple Class (25 mins)
# -------------------------------------------------
# 1. Define a class called 'Car'.
# 2. Add an __init__() method with three attributes:
#       - make
#       - model
#       - year
# 3. Create two car objects (instances) and print their attributes.
# 4. Add a __str__() method to display car details neatly when printed.

# Example:
#   car1 = Car("Toyota", "Corolla", 2020)
#   print(car1)
# Expected output: "2020 Toyota Corolla"


# -------------------------------------------------
# Task B: Adding Methods and Default Attributes (30 mins)
# -------------------------------------------------
# 1. Extend the Car class with:
#       - a default attribute: odometer_reading = 0
#       - a method 'read_odometer()' that prints the current mileage
#       - a method 'update_odometer(mileage)' that sets a new mileage
#         (prevent reducing the odometer!)
#       - a method 'increment_odometer(miles)' that adds to mileage
# 2. Demonstrate these methods by creating a car, updating mileage,
#    and printing results.


# -------------------------------------------------
# Task C: Mini Project – Student Record System (35 mins)
# -------------------------------------------------
# 1. Create a class called 'Student' with attributes:
#       - first_name
#       - last_name
#       - student_id
#       - grades (a list, default empty)
# 2. Add methods:
#       - add_grade(grade)
#       - average_grade() — returns the mean of all grades
#       - __str__() — prints student details and average
# 3. Create several Student objects and add grades for each.
# 4. Store all students in a list and print a report showing their details.
#
# Extension:
#   - Create a method 'is_passing()' that returns True if average >= 50.
#   - Print only passing students.

