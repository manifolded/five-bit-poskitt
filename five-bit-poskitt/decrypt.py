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
mask = ""
for bit in cleaned:
    if bit.isupper():
        mask += "1"
    else:
        mask += "0"

code = {'0':'00000', '1':'00001', '2':'00010', '3':'00011', '4':'00100', '5':'00101', \
    '6':'00110', '7':'00111', '8':'01000', '9':'01001', 'A':'01010', 'B':'01011', \
    'C':'01100', 'D':'01101', 'E':'01110', 'F':'01111', 'G':'10000', 'H':'10001', \
    'I':'10010', 'J':'10011', 'K':'10011', 'L':'10100', 'M':'10101', 'N':'10110', \
    'O':'10111', 'P':'11000', 'Q':'11000', 'R':'11001', 'S':'11010', 'T':'11011', \
    'U':'11100', 'V':'11101', 'W':'11110', 'X':'11110', 'Y':'11111', 'Z':'11111'}

# https://stackoverflow.com/questions/483666/python-reverse-invert-a-mapping
uncode = {v: k for k, v in code.iteritems()}

# read 'mask' by 5 bit "bytes" and apply uncode to get the decrypted message
message = ""
for i in xrange(0, len(mask), 5):
    message += uncode[mask[i:i+5]]
print message