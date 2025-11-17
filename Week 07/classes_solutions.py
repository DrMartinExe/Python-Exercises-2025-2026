# =========================================
# Week 7 Solutions — Object-Oriented Programming
# Save as solutions7.py
# =========================================

# --- Task A Solution ---
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


# Demonstrate creating car objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Focus", 2018)
print("Task A Results:")
print(car1)
print(car2)


# --- Task B Solution ---
class Car:
    """A more detailed car class with odometer and methods."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # default value

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set odometer reading to given value, reject rollbacks."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add given amount to odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("Miles must be positive.")


print("\nTask B Results:")
my_car = Car("Honda", "Civic", 2021)
print(my_car)
my_car.read_odometer()
my_car.update_odometer(15000)
my_car.read_odometer()
my_car.increment_odometer(500)
my_car.read_odometer()


# --- Task C Solution ---
class Student:
    """A simple representation of a student record."""

    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.grades = []  # default empty list

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_passing(self):
        return self.average_grade() >= 50

    def __str__(self):
        avg = self.average_grade()
        return (f"{self.first_name} {self.last_name} (ID: {self.student_id}) "
                f"— Average: {avg:.2f}")


# Create a few student objects
students = [
    Student("Alice", "Brown", "S001"),
    Student("Bob", "Green", "S002"),
    Student("Charlie", "White", "S003")
]

# Add some grades
students[0].add_grade(70)
students[0].add_grade(80)
students[1].add_grade(45)
students[1].add_grade(55)
students[2].add_grade(30)

# Print a simple report
print("\nTask C Results: Student Report")
for s in students:
    print(s)

# Print only passing students
print("\nPassing Students:")
for s in students:
    if s.is_passing():
        print(f"✅ {s.first_name} {s.last_name}")
