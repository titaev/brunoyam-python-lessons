import re

with open("page.html") as f:
    text = f.read()

parts = list(filter(lambda x: x != "", re.split(r"<li>(.*<ol>.*)</li>", text, flags=re.DOTALL)))
for part in parts:
    print(part)
    title = re.match(r"(.*)<ol>", part, flags=re.DOTALL).groups()[0]
    