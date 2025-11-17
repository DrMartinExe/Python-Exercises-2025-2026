# Week 8 – Files and Errors: Exercises

# Exercise 1 — Reading From a File
# --------------------------------
# You are given a text file called animals.txt containing one animal name per line.
# Tasks:
# 1. Read all lines into a list, stripping whitespace.
# 2. Print the total number of animals.
# 3. Print each animal in title case.
# 4. Handle FileNotFoundError with a friendly message.


# Exercise 2 — Writing & Appending to a File
# -------------------------------------------
# 1. Ask the user for three favourite foods.
# 2. Write them to favourites.txt (one per line).
# 3. Ask for one additional food and append it to the file.


# Exercise 3 — Handling ZeroDivisionError
# ---------------------------------------
# 1. Ask the user for two numbers.
# 2. Attempt to divide them using try-except.
# 3. Handle ZeroDivisionError and ValueError.
# 4. Use an else block to print result.
# 5. Repeat until the user types 'quit'.


# Exercise 4 — JSON Storage
# -------------------------
# 1. Ask the user for their name.
# 2. Store it in a dictionary and save to user.json using json.dumps().
# 3. Write another program to read user.json and welcome the user.
# 4. Fail silently if user.json does not exist.


# Exercise 5 — File Processing With Error Handling
# ------------------------------------------------
# Given numbers.txt containing one number per line (some invalid):
# 1. Read file line by line.
# 2. Convert to int inside try-except.
# 3. Store valid numbers.
# 4. Ignore invalid lines silently.
# 5. Print count, sum, and average of valid numbers.
