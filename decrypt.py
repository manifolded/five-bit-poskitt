#!/Users/keith/anaconda/envs/py2/bin/python
import sys
import string

# =======================================================================
# =======================================================================
# Get input from stdin
public = ""
for line in sys.stdin:
    #print line
    public += line

# Clean public - i.e. remove whitespace and punctuation
cleaned = ""
for char in public:
    if not char.isspace() and not char in string.punctuation:
        cleaned += char

# Extract upper/lowercase state data
encrypted = ""
for bit in cleaned:
    if bit.isupper():
        encrypted += "1"
    else:
        encrypted += "0"

print encrypted