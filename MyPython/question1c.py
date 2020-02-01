import re

x = raw_input("Enter a sequence:")
print re.sub("wh[a-z]*","WH-word", x)
