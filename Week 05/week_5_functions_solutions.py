# Week 5: Functions — Solutions
# These solutions show correct usage and explanations for each exercise.

# =============================
# EXERCISE 1: Defining Functions
# =============================
def greet_user():
    print("Hello!")

# Calling the function
print("--- Exercise 1 ---")
greet_user()
greet_user()

# =============================
# EXERCISE 2: Passing Arguments
# =============================
def greet_user(name):
    print(f"Hello, {name}!")

print("--- Exercise 2 ---")
greet_user("Alice")  # positional argument
greet_user(name="Bob")  # keyword argument

# =============================
# EXERCISE 3: Default Values
# =============================
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

print("--- Exercise 3 ---")
greet_user()
greet_user("Charlie")

# =============================
# EXERCISE 4: Returning Values
# =============================
def make_full_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

print("--- Exercise 4 ---")
name = make_full_name("ada", "lovelace")
print(name)

# =============================
# EXERCISE 5: Returning a Dictionary
# =============================
def make_full_name_dict(first, last):
    person = {'first': first, 'last': last}
    return person

print("--- Exercise 5 ---")
print(make_full_name_dict("Ada", "Lovelace"))

# =============================
# EXERCISE 6: Working with Lists
# =============================
def print_models(models_to_print):
    print("Printing models:")
    while models_to_print:
        current = models_to_print.pop()
        print(f"Model printed: {current}")

print("--- Exercise 6 ---")
models = ['Phone Case', 'Drone', 'Robot']
print_models(models[:])  # copy to preserve original
print(f"Remaining models: {models}")

# =============================
# EXERCISE 7: Preventing Modification
# =============================
def print_models_safe(models_to_print):
    print("Printing models (safe copy):")
    for model in models_to_print:
        print(f"Model: {model}")

print("--- Exercise 7 ---")
print_models_safe(models[:])
print(f"Original list still intact: {models}")

# =============================
# EXERCISE 8: Arbitrary Arguments
# =============================
def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

print("--- Exercise 8 ---")
make_pizza('pepperoni')
make_pizza('mushrooms', 'onions', 'olives')

# =============================
# EXERCISE 9: Arbitrary Keyword Arguments
# =============================
def build_profile(first, last, **info):
    profile = {'first_name': first, 'last_name': last}
    profile.update(info)
    return profile

print("--- Exercise 9 ---")
user_profile = build_profile('Albert', 'Einstein', location='Princeton', field='Physics')
print(user_profile)

# =============================
# EXERCISE 10: Modules
# =============================
# In a separate file (my_functions.py):
# def greet_user(name):
#     print(f"Hello, {name}! Welcome back.")

# Importing the module in another script:
# import my_functions
# my_functions.greet_user('Alice')

# Or importing a specific function:
# from my_functions import greet_user
# greet_user('Bob')

# Or using an alias:
# import my_functions as mf
# mf.greet_user('Charlie')

# =============================
# BONUS CHALLENGE
# =============================
def build_user_profile(**user_data):
    return user_data

def greet_from_module(name):
    print(f"Welcome, {name}! Thanks for joining.")

print("--- Bonus Challenge ---")
profile = build_user_profile(name='Diana', age=30, city='London')
greet_from_module(profile['name'])
print(profile)
