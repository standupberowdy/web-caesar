"""
# input validation functions
# https://www.owasp.org/index.php/Input_Validation_Cheat_Sheet
# - removes potentially hazardous characters
def sanitise_text_input(s):
    import re, html
    allowed_characters = "a-zA-Z0-9\_\,\s\.\-\!\?"
    s = re.sub(r'[^{}]+'.format(allowed_characters), '', s)
    return html.escape(s)
# - removes any non-numeric numbers and converts the string to an int
def sanitise_number_input(n):
    import re
    allowed_characters = "0-9"
    n = re.sub(r'[^{}]+'.format(allowed_characters), '', str(n))
    try:
        return int(n)
    except ValueError:
        return 0

"""
def alphabet_position(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower = character.lower()
    return alphabet.index(lower)

def rotate_string_13(text):

    rotated = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in text:
        rotated_idx = (alphabet_position(char) + 13) % 26
        if char.isupper():
            rotated = rotated + alphabet[rotated_idx].upper()
        else:
            rotated = rotated + alphabet[rotated_idx]

    return rotated

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_idx = (alphabet_position(char) + rot) % 26

    if char.isupper():
        return alphabet[rotated_idx].upper()
    else:
        return alphabet[rotated_idx]

def rotate_string(text, rot):

    rotated = ''

    for char in text:
        if (char.isalpha()):
            rotated = rotated + rotate_character(char, rot)
        else:
            rotated = rotated + char

    return rotated
