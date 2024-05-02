"""
File: my_functions.py
Author: Dave Cheng
Date: 2024-05-02
Description: Functions for LiveHack performance task.
"""


def generate_acronym(phrase, with_periods=False):
    """
    Generate an acronym from a given phrase.
    
    Parameters:
        phrase (str): The phrase from which to generate the acronym.
        with_periods (bool, optional): If True, add periods after each letter in the acronym. Default is False.
    
    Returns:
        str: The acronym generated from the input phrase.
    """
    # Initialize an empty acronym
    acronym = ""

    # Initialize a flag to track whether the current character is the start of a new word
    new_word = True

    # Iterate over each character in the phrase
    for char in phrase:
        # Check if the current character is a space (indicating the end of a word)
        if char == " ":
            new_word = True
        # Check if the current character is not a space and it's the start of a new word
        elif new_word:
            # Add the uppercase version of the character to the acronym
            acronym += char.upper()
            # If with_periods is True, add a period
            if with_periods:
                acronym += "."
            # Set the flag to False, indicating that subsequent characters are not the start of a new word
            new_word = False

    return acronym


def is_lucky(number):
    """
    Check if a number is lucky, meaning it contains the digit 8 but not the digit 4.
    
    Parameters:
        number (int): The number to check for luckiness.
    
    Returns:
        bool: True if the number is lucky, False otherwise.
    """
    # Convert the number to a string to check each digit
    number_str = str(number)
    
    # Check if the number contains a 4
    if '4' in number_str:
        return False
    
    # Check if the number contains an 8
    if '8' in number_str:
        # If there's an 8 and no 4, it's lucky
        if '4' not in number_str:
            return True
        # If there's an 8 and also a 4, it's unlucky
        else:
            return False
    
    # If the number contains neither 4 nor 8, it's unlucky
    return False
