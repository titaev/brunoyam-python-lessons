import re

text = "asdf fjdk;afed,fjek,asdf,foo"
result = re.split("[;, ]", text)
print(result)