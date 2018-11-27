import re

text = "AV is largest Analytics community of India"
result = re.findall(r"\b[aeiouyAEIOUY]\w+", text)
print(result)
