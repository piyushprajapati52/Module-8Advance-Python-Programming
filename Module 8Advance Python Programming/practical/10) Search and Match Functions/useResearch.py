# Write a Python program to search for a word in a string using
# re.search(). 

import re

text = "Python is a powerful programming language."

word = "powerful"

match = re.search(word, text)

if match:
    print(f"Word '{word}' found at position {match.start()} to {match.end()}")
else:
    print(f" Word '{word}' not found.")