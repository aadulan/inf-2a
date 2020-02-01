import re # imports the pattern matching

x=raw_input("Enter a sequence :") # lets the user enter a sequence.
print re.match("(0|1)(0|1)(0|1)([a-z]|[0-9])*",x) # prints the result of the match
