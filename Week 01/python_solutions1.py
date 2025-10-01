# ==============================
# Beginner Python Solutions
# ==============================
# Save this file as solutions.py

# Exercise 1: Variables
name = "Alice"
print(name)

# Exercise 2: Numbers
x = 5
y = 10
print(x, y)

# Exercise 3: Arithmetic Operators
print("Sum:", x + y)
print("Difference:", x - y)
print("Product:", x * y)
print("Quotient:", x / y)

# Exercise 4: Strings
greeting = "Hello"
person = "Alice"
print(greeting + " " + person)

# Exercise 5: Comments
# This line prints my name
print("Alice")

# Exercise 6: Logical Operators
is_sunny = True
is_warm = False
print(is_sunny and is_warm)  # AND
print(is_sunny or is_warm)   # OR
print(not is_sunny)          # NOT

# Exercise 7: Combining Concepts
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")

# Exercise 8: Challenge
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)
print("First is greater:", num1 > num2)
print("Numbers are equal:", num1 == num2)

# Extra Challenge 1
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name + ", you will be", age + 1, "next year.")

# Extra Challenge 2
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Extra Challenge 3
word1 = "Python"
word2 = "Rocks"
print("Total characters:", len(word1) + len(word2))

# Extra Challenge 4
age = int(input("Enter your age: "))
is_sunny = input("Is it sunny? (True/False): ")
is_sunny = is_sunny == "True"
if age >= 12 and is_sunny:
    print("You are allowed to go outside.")
else:
    print("You are not allowed to go outside.")

# Final Project: Mini Program
name = input("Enter your name: ")
print("Hello,", name + "!")

age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)

print("Goodbye,", name + "! Thanks for using the program.")
