# ==========================================
# Week 4: Control Flow and User Input
# ==========================================
# Save this file as exercises4.py
# Topics:
#   * if Statements and Boolean expressions
#   * Dictionaries
#   * Nesting
#   * User Input
#   * while Loops
# Learning Objectives:
#   * Write programs that make decisions
#   * Store and manage data with dictionaries
#   * Create interactive loops that respond to user input

# ==========================================
# Exercise 1: Simple if Statements
# ------------------------------------------
# Create a variable age = 18
# Write an if statement that prints "You are old enough to vote!"
# if age is greater than or equal to 18.
# Otherwise, print "You are not old enough to vote yet."


# ==========================================
# Exercise 2: if-elif-else Chains
# ------------------------------------------
# Create a variable temperature = 25
# Write an if-elif-else chain that:
#   * prints "It's cold!" if temperature < 10
#   * prints "It's mild." if temperature is between 10 and 25
#   * prints "It's hot!" if temperature > 25


# ==========================================
# Exercise 3: Boolean Expressions
# ------------------------------------------
# Create two variables: is_raining = True and have_umbrella = False
# Write an if-else statement:
#   * If it's raining and you have an umbrella, print "You're good to go!"
#   * If it's raining and you don't have one, print "You might get wet!"
#   * Otherwise, print "No rain today!"


# ==========================================
# Exercise 4: Using if with Lists
# ------------------------------------------
# Create a list of fruits = ['apple', 'banana', 'cherry']
# Ask the user to input a fruit name.
# If the fruit is in the list, print "Yes, we have that!"
# Otherwise, print "Sorry, we don't have that."


# ==========================================
# Exercise 5: Dictionaries - Basics
# ------------------------------------------
# Create a dictionary called person with keys: 'name', 'age', and 'city'.
# Print each key-value pair in a formatted sentence, e.g.:
#   "Name: Alice, Age: 25, City: London"


# ==========================================
# Exercise 6: Adding and Modifying Dictionary Entries
# ------------------------------------------
# Add a new key 'occupation' with a value to your dictionary.
# Change the value of 'city' to something new.
# Print the updated dictionary.


# ==========================================
# Exercise 7: Using get() Safely
# ------------------------------------------
# Try to access a key called 'country' using person.get('country', 'Not specified').
# Print the result.


# ==========================================
# Exercise 8: Looping Through a Dictionary
# ------------------------------------------
# Create a dictionary of favorite_languages:
#   favorite_languages = {'Alice': 'Python', 'Bob': 'C', 'Charlie': 'JavaScript'}
# Loop through the dictionary and print:
#   "Alice's favorite language is Python."


# ==========================================
# Exercise 9: Nesting - Dictionaries in Dictionaries
# ------------------------------------------
# Create a dictionary users = {
#     'alice': {'age': 25, 'city': 'London'},
#     'bob': {'age': 30, 'city': 'New York'}
# }
# Loop through the dictionary and print each user's name and details.


# ==========================================
# Exercise 10: User Input
# ------------------------------------------
# Ask the user for their name using input().
# Greet them by name, e.g. "Hello, Sam!"


# ==========================================
# Exercise 11: Using int() and Modulo Operator
# ------------------------------------------
# Ask the user for a number using input().
# Convert it to an integer.
# If the number is even, print "That’s an even number!"
# Otherwise, print "That’s an odd number!"


# ==========================================
# Exercise 12: while Loops
# ------------------------------------------
# Write a while loop that asks for input repeatedly until the user types 'quit'.
# Echo back each message they type (except 'quit').


# ==========================================
# Exercise 13: Using Flags and break
# ------------------------------------------
# Modify the previous exercise using a flag (e.g., active = True).
# Inside the loop, if the user types 'quit', set active = False to stop the loop.


# ==========================================
# Exercise 14: while Loops with Lists
# ------------------------------------------
# Create a list of unconfirmed_users = ['alice', 'bob', 'charlie']
# and an empty list confirmed_users = []
# Use a while loop to move each user from unconfirmed_users to confirmed_users.
# Print messages confirming each user has been verified.


# ==========================================
# Final Challenge: Interactive Program
# ------------------------------------------
# Create a small dictionary of menu items with prices, e.g.:
#   menu = {'coffee': 2.5, 'tea': 2.0, 'cake': 3.5}
# Write a program that:
#   * Repeatedly asks the user to enter an item or 'quit' to stop.
#   * If the item exists, print its price.
#   * If not, print "Sorry, we don't have that."
#   * When the user quits, thank them for visiting.
