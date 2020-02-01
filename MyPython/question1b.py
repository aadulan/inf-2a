import re

x = raw_input ("Enter a sequence :")
print re.findall("[a-z]*ly", x)
