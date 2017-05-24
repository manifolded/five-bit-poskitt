import string
from pandas import read_csv

# =======================================================================
# Reads text from file in to a string, ignoring punctuation and whitespace, and converting
# all characters to uppercase.
def importTextAndStripToCaps(filename):
    #from https://stackoverflow.com/questions/2988211/how-to-read-a-single-character-at-a-time-from-a-file-in-python
    #Also:
    #   for whitespace removal: https://www.tutorialspoint.com/python/string_isspace.htm
    #   for punctuation removal: https://www.dotnetperls.com/punctuation-python
    #   to Upper Case letters: https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase

    result = ""
    with open(filename) as file:
        while True:
            c = file.read(1)
            if not c:
                #print "End of file."
                break
            if c.isspace():
                continue
            if c in string.punctuation:
                continue
            #print c.upper()
            result += c.upper()
    return result

# =======================================================================
# Performs replacements on a string, where those replacements are specified by a 
# dictionary.
# https://stackoverflow.com/questions/6116978/python-replace-multiple-strings
def constructMask(message, code):
    result = ""
    for c in message:
        result += code[c]
    return result

# =======================================================================
# Outputs the string, text, where the case (upper/lower) for each character is set 
# by the value of the mask array (either '1' or '0').
def encodeInCaps(text, mask):
    result = ""
    text_it = text.iter()
    for m in mask:
        if m=='1':
            result += text_it.upper()
        else:
            result += text_it.lower()
        ++text_it
        if !text_it: # @TODO - This is intended to check if we've reached the end of 
        # the string and if so, bring us back to the beginning, but the syntax is 
        # wrong.  Ugh.
            text_it = text.begin()            
    return result

# =======================================================================
# =======================================================================
# Main code begins here:

text = importTextAndStripToCaps("lorem_ipsum.txt")
# print text

message = importTextAndStripToCaps("message.txt")

# we'll use pandas to read the code in from file
# to prevent dropping leading zeros: 
#   https://stackoverflow.com/questions/13250046/pandas-csv-import-keep-leading-zeros-in-a-column
temp = read_csv('code.csv', sep='\t', header=1)
#print temp

code = dict(zip(temp[0], temp[1]))
# print code

# @TODO - This line should not generate an error!
print code["C"]

msgMask = constructMask(message, code)
# print msgMask

print encodeInCaps(text, msgMask)

