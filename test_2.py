"""
File: test_2.py
Description: Test cases and expected output for use with the function in
             my_functions.py. 
             
             Note that if you have written the function definition 
             correctly, you should not have to touch this file at all. 
             Just run it and observe the output. Check if the output
             matches the correct, expected output in the comments below.
"""

# Import the function (make sure you've defined it in the other file)
from my_functions import generate_acronym


# Example usage and expected results

print(generate_acronym("York Catholic District School Board"))  
# Output: YCDSB

my_word = generate_acronym("World Health Organization", False)
print(my_word)
# Output: WHO

print(generate_acronym("Too much information", True))
# Output: T.M.I.

my_motto = generate_acronym("you only live once")
print(my_motto)
# Output: YOLO

print(generate_acronym("i don't know"))
# Output: IDK

print(generate_acronym("BE RIGHT BACK", False))
# Output: BRB

print(generate_acronym("OH my GOD", True))
# Output: O.M.G.
