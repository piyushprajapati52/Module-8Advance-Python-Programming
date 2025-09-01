#  Write a Python program to match a word in a string using re.match().

import re

text = "Python is a powerful programming language."

word = "Python"

match = re.match(word, text)

if match:
    print(f"Word '{word}' matched at position {match.start()} to {match.end()}")
else:
    print(f"Word '{word}' not found at the beginning.")