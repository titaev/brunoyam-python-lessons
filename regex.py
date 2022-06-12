# Написать регулярное выражение для извлечения из текста всех email-адресов.

# import re
# s = 'По всем вопросам пишите на vasiliy-pupkin@gmail.com, или на secondemail@yandex.ru, отвечу сразу. Или пишите моему ассистенту secretary@gmail.com!'
# emails = re.findall(r'[\w\.-]+@[\w\.-]+', s)
# for email in emails:
#     print(email)

# Дана последовательность строк. Нужно вывести те, в которых «кот» встречается в качестве отдельного слова.

import re
list_str = ['кот в сапогах',
'кошка и кот',
'котофей',
'котяра']
for line in list_str:
    line = line.rstrip()
    if re.search(r"\bкот\b", line):
        print(line)