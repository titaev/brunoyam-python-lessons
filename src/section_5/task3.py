import re

text = "abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz"
result = re.findall(r"[\w\.]+@\w+\.\w+", text)
print(result)