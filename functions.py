# Function: add_numbers
def add_numbers(num1, num2):
    """
    Return the sum of num1 and num2.
    
    Args:
        num1 (int or float): The first number.
        num2 (int or float): The second number.
    
    Returns:
        int or float: The sum of num1 and num2.
    
    Example:
        >>> add_numbers(5, 3)
        8
    """
    return num1 + num2

result = add_numbers(5, 3)
print(result)


# Function: is_even
def is_even(number):
    """
    Return True if the number is even, otherwise False.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is even, False otherwise.
    
    Example:
        >>> is_even(4)
        True
        >>> is_even(9)
        False
    """
    return number % 2 == 0

result = is_even(9)
print(result)


# Function: reverse_string
def reverse_string(text):
    """
    Return the reversed version of the input string text.
    
    Args:
        text (str): The string to reverse.
    
    Returns:
        str: The reversed string.
    
    Example:
        >>> reverse_string("pauline")
        "eniluap"
    """
    return text[::-1]

result = reverse_string("pauline")
print(result)


# Function: count_vowels
def count_vowels(text):
    """
    Return the count of vowels in the input string text. 
    Vowels are 'a', 'e', 'i', 'o', 'u' (case-insensitive).
    
    Args:
        text (str): The string to count vowels in.
    
    Returns:
        int: The count of vowels in the string.
    
    Example:
        >>> count_vowels("pauline")
        4
        >>> count_vowels("PAULINE")
        4
    """
    vowels = set('aeiou') 
    count = 0
    for char in text.lower():  # Convert text to lowercase for case insensitivity
        if char in vowels:
            count += 1
    return count

result = count_vowels("pauline")
print(result)
result = count_vowels("PAULINE")
print(result)


# Function: calculate_factorial
def calculate_factorial(n):
    """
    Return the factorial of a non-negative integer n.
    
    Args:
        n (int): The non-negative integer to compute the factorial of.
    
    Returns:
        int: The factorial of n.
    
    Example:
        >>> calculate_factorial(5)
        120
    """
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

result = calculate_factorial(5)
print(result)


# Function: apply_decorator
def decorator_func(func):
    """
    Decorator that prints a message before calling the original function.
    
    Args:
        func (function): The function to be decorated.
    
    Returns:
        function: A wrapper function that prints a message and then calls the original function.
    """
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper


def apply_decorator(func):
    """
    Apply the decorator to a given function.
    
    Args:
        func (function): The function to which the decorator should be applied.
    
    Returns:
        function: A decorated version of the input function.
    """
    return decorator_func(func)


# Define a sample function to apply the decorator to
def sample_function():
    """
    Sample function that returns a specific string.
    
    Returns:
        str: A specific string.
    """
    return "Bravo Pauline!"


# Apply the decorator to the sample function
decorated_function = apply_decorator(sample_function)

# Call the decorated function and print the result
result = decorated_function()
print(result)


# Sequences; Sort List of Tuples
def sort_by_age(list_of_tuples):
    """
    Sort a list of (name, age) tuples by age in ascending order.
    
    Args:
        list_of_tuples (list of tuple): List where each tuple contains a name and an age.
    
    Returns:
        list of tuple: The sorted list of tuples by age.
    
    Example:
        >>> sort_by_age([("Alice", 30), ("Bob", 25)])
        [('Bob', 25), ('Alice', 30)]
    """
    return sorted(list_of_tuples, key=lambda x: x[1])


example_list = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

result = sort_by_age(example_list)
print(result)


# Sets, Dictionaries; Merge Dictionaries
def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries. If keys overlap, sum their values.
    
    Args:
        dict1 (dict): The first dictionary to merge.
        dict2 (dict): The second dictionary to merge.
    
    Returns:
        dict: A new dictionary with merged key-value pairs. If keys overlap, their values are summed.
    
    Example:
        >>> merge_dicts({'a': 10}, {'a': 20, 'b': 30})
        {'a': 30, 'b': 30}
    """
    merged = dict1.copy()  # Start with a copy of the first dictionary

    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Sum the values if key is already in merged
        else:
            merged[key] = value  # Add the new key-value pair

    return merged


dict1 = {'a': 10}
dict2 = {'a': 20, 'b': 30}

result = merge_dicts(dict1, dict2)
print(result)


# Object-Oriented Programming; Class Creation
class Car:
    """
    A class representing a car.

    Attributes:
        make (str): The make of the car.
        model (str): The model of the car.
        year (int): The year of manufacture.
    """

    def __init__(self, make, model, year):
        """
        Initialize a new Car instance with make, model, and year.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            year (int): The year of manufacture.
        """
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        """
        Print out the car's information.

        Example:
            "2020 Toyota Camry"
        """
        print(f"{self.year} {self.make} {self.model}")

    def __str__(self):
        """
        Return a string representation of the car's information.

        Returns:
            str: The car's information.
        """
        return f"{self.year} {self.make} {self.model}"


# Example usage:
car = Car("Toyota", "Camry", 2020)
print(car)
