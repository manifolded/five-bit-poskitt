#!/usr/bin/python2
import string
from pandas import read_csv
from itertools import cycle

# =======================================================================
# Performs replacements on a string, where those replacements are specified by a 
# dictionary.
def constructMask(msg, cde):
    result = ""
    for c in msg:
        # @TODO - Must handle case where c is not in cde.
        result += cde[c]
    return result

# =======================================================================
# Outputs the string, txt, where the case (upper/lower) for each character is set 
# by the value of the mask array (either '1' or '0').
def encodeInCaps(txt, mask):
    char = ""
    result = ""
    txt_it = cycle(txt)
    for m in mask:
        char = txt_it.next()
        while char.isspace():
            result += char
            char = txt_it.next()
        if m == '1':
            result += char.upper()
        else: # i.e. m == '0'
            result += char.lower()

    return result

# =======================================================================
# =======================================================================
# Main code begins here:

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor " \
+"incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud " \
+"exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute " \
+"irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla " \
+"pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia " \
+"deserunt mollit anim id est laborum"
message = "RECOVERMEMCHIPSFURMANRETURNMATTHEWSSERINACRUCIAL"
code = {'0':'00000', '1':'00001', '2':'00010', '3':'00011', '4':'00100', '5':'00101', 
    '6':'00110', '7':'00111', '8':'01000', '9':'01001', 'A':'01010', 'B':'01011', 
    'C':'01100', 'D':'01101', 'E':'01110', 'F':'01111', 'G':'10000', 'H':'10001',
    'I':'10010', 'J':'10011', 'K':'10011', 'L':'10100', 'M':'10101', 'N':'10110',
    'O':'10111', 'P':'11000', 'Q':'11000', 'R':'11001', 'S':'11010', 'T':'11011',
    'U':'11100', 'V':'11101', 'W':'11110', 'X':'11110', 'Y':'11111', 'Z':'11111'}

msgMask = constructMask(message, code)
print encodeInCaps(text, msgMask)

