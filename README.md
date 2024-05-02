# ICS3U LiveHack 2 - Practice

For this LiveHack, you will be writing functions with parameters and return values. Do all of your work in the file `my_functions.py` in this repo. 

Do not modify any of the code in `test_1.py` or `test_2.py`. If your functions are written properly, the tests in each of these files will run without errors, giving the expected output as annotated in the comments.

Make sure to document your code, including writing a complete **docstring** for your function definitions.



## Problem 1: Lucky Numbers

In Chinese culture, the number 8 is considered lucky because it is pronounced similarly to the word for "wealth" and "prosperity". Chinese speakers often place particular emphasis on the number's auspicious qualities. For example, houses with street addresses containing the number 8 often appeal more to some Chinese buyers because of this superstition.

Likewise, the number 4 is considered unlucky because it sounds like "death". Some Las Vegas hotels like the Encore and the Wynn even go so far as to skip the 40th to 49th floors in their numbering.

![turning red](images/turning_red.jpg)

Write a function that takes an single parameter of an integer number. It then returns a boolean result of whether or not the number is lucky, based on these rules:

- If there is a 4 anywhere in the number, it is unlucky, thus return False.
- If there is an 8 anywhere in the number, and no 4, it is lucky, thus return True.
- If there is an 8 anywhere in the number, and also a 4, it is unlucky, thus return False.

### Example Usage
You can use the test cases in `test_1.py`, shown below. Do not modify any of the code in `test_1.py`. Simply run the file and check if your output matches the expected output in the comments.

#### Test cases in `test_1.py`
```python
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
```

#### Output of running `test_1.py`
```
False
False
True
False
False
True
True
True
False
Very lucky!
```

<br><br>

## Problem 2: Acronym Generator

Write a function that generates an acronym from a given phrase. The function should take a string as input and return the acronym formed by the initial letters of each word in the phrase.

- The function should be called `generate_acronym`. Write it in the file `my_functions.py`.
- Use two parameters: (1) First parameter is the phrase as a string. (2) Second parameter is a boolean that changes whether or not the function returns the result with periods. **Default** should be no periods.
- Return a string with the resulting acronym.
- You can assume the function will never be called with an blank phrase. 
- Words will always be separated by a blank space character.
- Phrases may have upper and lower case letters.
- Return result should always be uppercase.

### Example Usage
You can use the test cases in `test_2.py`, shown below. Do not modify any of the code in `test_2.py`. Simply run the file and check if your output matches the expected output in the comments.

#### Test cases in `test_2.py`
```python
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
```

#### Output of running `test_2.py`
```
YCDSB
WHO
T.M.I.
YOLO
IDK
BRB
O.M.G.
```
