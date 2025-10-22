# Week 5: Functions
# Learning Objectives:
# - Define and use functions.
# - Pass arguments (positional, keyword, and with default values).
# - Return values from functions.
# - Work with lists inside functions.
# - Use *args and **kwargs.
# - Organize code into modules.

# =============================
# EXERCISE 1: Defining Functions
# =============================
# Task: Define a simple function called greet_user() that prints a greeting.
# Call it twice with different names.



# =============================
# EXERCISE 2: Passing Arguments
# =============================
# Task: Modify greet_user() so it accepts one parameter 'name' and prints a personalized greeting.
# Call it using both positional and keyword arguments.



# =============================
# EXERCISE 3: Default Values
# =============================
# Task: Give your function a default value for 'name' (e.g., 'Guest').
# Test calling it with and without providing a name.



# =============================
# EXERCISE 4: Returning Values
# =============================
# Task: Define a function called make_full_name(first, last) that returns a formatted full name.
# Print the returned value.



# =============================
# EXERCISE 5: Returning a Dictionary
# =============================
# Task: Modify make_full_name() to return a dictionary with keys 'first' and 'last'.
# Print the result.



# =============================
# EXERCISE 6: Working with Lists
# =============================
# Task: Define a function called print_models(models_to_print) that loops through and prints each model name.
# Pass in a list of model names. Observe how lists behave when passed to functions.



# =============================
# EXERCISE 7: Preventing Modification
# =============================
# Task: Modify print_models() to work on a *copy* of the list so the original is not changed.
# Hint: Pass models_to_print[:] to the function.



# =============================
# EXERCISE 8: Arbitrary Arguments
# =============================
# Task: Define a function called make_pizza(*toppings) that prints all the toppings requested.
# Call it with different numbers of arguments.



# =============================
# EXERCISE 9: Arbitrary Keyword Arguments
# =============================
# Task: Define a function called build_profile(first, last, **info) that stores any number of keyword-value pairs.
# Test it with different pieces of user data.



# =============================
# EXERCISE 10: Modules
# =============================
# Task: Create a separate Python file called 'my_functions.py' with a simple function (e.g., greet_user()).
# Import that function in this script and call it.
# Try importing:
#   - the whole module
#   - a specific function
#   - a function using an alias



# =============================
# BONUS CHALLENGE
# =============================
# Task: Combine what you’ve learned.
# Write a program that:
#   - Defines a function to collect user info (name, age, city)
#   - Stores it in a dictionary using **kwargs
#   - Prints a greeting using a function from another module
