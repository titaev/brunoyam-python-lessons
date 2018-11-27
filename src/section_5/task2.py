import re

text = "AV is largest Analytics community of India"
result = re.findall(r"\b\w{2}", text)
print(result)