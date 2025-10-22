# ==========================================
# Week 4 Solutions: Control Flow and User Input
# ==========================================
# Save this file as solutions4.py

# Exercise 1: Simple if Statements
age = 18
if age >= 18:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote yet.")

# Exercise 2: if-elif-else Chains
temperature = 25
if temperature < 10:
    print("It's cold!")
elif temperature <= 25:
    print("It's mild.")
else:
    print("It's hot!")

# Exercise 3: Boolean Expressions
is_raining = True
have_umbrella = False
if is_raining and have_umbrella:
    print("You're good to go!")
elif is_raining and not have_umbrella:
    print("You might get wet!")
else:
    print("No rain today!")

# Exercise 4: Using if with Lists
fruits = ['apple', 'banana', 'cherry']
fruit_input = input("Enter a fruit: ")
if fruit_input.lower() in fruits:
    print("Yes, we have that!")
else:
    print("Sorry, we don't have that.")

# Exercise 5: Dictionaries - Basics
person = {'name': 'Alice', 'age': 25, 'city': 'London'}
print(f"Name: {person['name']}, Age: {person['age']}, City: {person['city']}")

# Exercise 6: Adding and Modifying Dictionary Entries
person['occupation'] = 'Engineer'
person['city'] = 'Manchester'
print(person)

# Exercise 7: Using get() Safely
country = person.get('country', 'Not specified')
print(country)

# Exercise 8: Looping Through a Dictionary
favorite_languages = {'Alice': 'Python', 'Bob': 'C', 'Charlie': 'JavaScript'}
for name, language in favorite_languages.items():
    print(f"{name}'s favorite language is {language}.")

# Exercise 9: Nesting - Dictionaries in Dictionaries
users = {
    'alice': {'age': 25, 'city': 'London'},
    'bob': {'age': 30, 'city': 'New York'}
}
for username, details in users.items():
    print(f"\nUsername: {username}")
    for key, value in details.items():
        print(f"  {key.title()}: {value}")

# Exercise 10: User Input
name = input("What is your name? ")
print(f"Hello, {name}!")

# Exercise 11: Using int() and Modulo Operator
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("That’s an even number!")
else:
    print("That’s an odd number!")

# Exercise 12: while Loops
message = ""
while message != 'quit':
    message = input("Enter a message (or 'quit' to exit): ")
    if message != 'quit':
        print(f"You said: {message}")

# Exercise 13: Using Flags and break
active = True
while active:
    message = input("Type something (or 'quit' to stop): ")
    if message == 'quit':
        active = False
    else:
        print(f"You typed: {message}")

# Exercise 14: while Loops with Lists
unconfirmed_users = ['alice', 'bob', 'charlie']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop(0)
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())

# Final Challenge: Interactive Program
menu = {'coffee': 2.5, 'tea': 2.0, 'cake': 3.5}
print("Welcome to the Café! Type 'quit' to exit.")
while True:
    order = input("What would you like to order? ").lower()
    if order == 'quit':
        print("Thanks for visiting!")
        break
    elif order in menu:
        print(f"A {order} costs £{menu[order]}")
    else:
        print("Sorry, we don't have that.")
