"""
File: test_1.py
Description: Test cases and expected output for use with the function in
             my_functions.py. 
             
             Note that if you have written the function definition 
             correctly, you should not have to touch this file at all. 
             Just run it and observe the output. Check if the output
             matches the correct, expected output in the comments below.
"""

# Import the function (make sure you've defined it in the other file)
from my_functions import is_lucky

# Example usage:
print(is_lucky(4872))  # Output: False
print(is_lucky(84321)) # Output: False
print(is_lucky(888))   # Output: True
print(is_lucky(456))   # Output: False
print(is_lucky(123))   # Output: False
print(is_lucky(8))     # Output: True
print(is_lucky(28))    # Output: True
print(is_lucky(128))   # Output: True
print(is_lucky(8888888488))   # Output: False

# Example usage in a small program
my_number = 128

if is_lucky(my_number):
    print("Very lucky!")
else:
    print("Not lucky!")
# Output: Very Lucky!