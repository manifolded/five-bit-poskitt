#!/Users/keith/anaconda/bin/python2.7
from string import ascii_lowercase
from prettytable import PrettyTable
# pylint: disable=C0103

# http://www.sitesbay.com/python-program/python-print-alphabet-pattern-in-python

def ciphertext(offset):
    ciphertext = [str(offset)]
    for i in range(0, 26):
        ciphertext.append(chr(65+(i+offset)%26))
    return ciphertext

def blanktext():
    blanktext = [" "]
    for i in range(0, 26):
        blanktext.append(" ")
    return blanktext

# construct the plaintext header
plaintext = [" "]
for i in range(0, 26):
    plaintext.append(ascii_lowercase[i])

# construct the table/grid
x = PrettyTable(plaintext)
x.padding_width = 1 # One space between column edges and contents (default)

# make all columns centered
for colHeader in plaintext:
    x.align[colHeader] = "c"

# construct the ciphertext body
x.add_row(blanktext())
for j in range(0, 26):
    x.add_row(ciphertext(j+1))

print x.get_html_string(attributes = {"class": "grid-style"})
# print x
