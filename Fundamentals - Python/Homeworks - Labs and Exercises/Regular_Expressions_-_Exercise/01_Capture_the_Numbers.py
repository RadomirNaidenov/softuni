import re

pattern = r'\d+'

data = input()

while True:
    if data:
        match = re.findall(pattern, data)
        if match:
            print(*match, end=" ")

        data = input()
    else:
        break       

