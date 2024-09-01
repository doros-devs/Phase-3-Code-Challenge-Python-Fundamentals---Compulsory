from math import factorial

import self


def add_numbers(num1, num2):
    return num1 + num2

def is_even(number):
    return number % 2 == 0

def reverse_string(string):
    return string[::-1]

def count_vowels(text):
    vowels = "aeiou"
    count = sum(1 for char in text.lower() if char in vowels)
    return count

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def decorator_func(f):
    def wrapper (*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper()

def apply_decorator(func):
    decorator_func= decorator_func(func)
    return decorator_func

def sort_by_age(num):
    return sorted(num, key=lambda x:x[1])

def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

class Car:
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

if __name__ == "__main__":
    # Test add_numbers
    print(add_numbers(3, 5))  # Output: 8

    # Test is_even
    print(is_even(4))  # Output: True
    print(is_even(7))  # Output: False

    # Test reverse_string
    print(reverse_string("hello"))  # Output: "olleh"

    # Test count_vowels
    print(count_vowels("hello world"))  # Output: 3

    # Test calculate_factorial
    print(calculate_factorial(5))  # Output: 120

    # Test apply_decorator
    @apply_decorator
    def greet():
        print("Hello, World!")

    greet()  # Output: "Decorator Applied" "Hello, World!"

    # Test sort_by_age
    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    print(sort_by_age(people))  # Output: [("Bob", 25), ("Alice", 30), ("Charlie", 35)]

    # Test merge_dicts
    dict1 = {'a': 100, 'b': 200}
    dict2 = {'b': 300, 'c': 400}
    print(merge_dicts(dict1, dict2))  # Output: {'a': 100, 'b': 500, 'c': 400}

    # Test Car class
    my_car = Car("Toyota", "Corolla", 2020)
    my_car.display_info()  # Output: "Car Information: 2020 Toyota Corolla"
