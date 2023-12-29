import re

text = "Применить (0)"
match = re.search(r'\((\d+)\)', text)
# match = None
if match:
        number = match.group(1)
        print(type(number), number)
else:
    print("None")