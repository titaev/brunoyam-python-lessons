import re

text = "AV is largest Analytics community of India"
match = re.match("\w+", text)
print(match.group())
