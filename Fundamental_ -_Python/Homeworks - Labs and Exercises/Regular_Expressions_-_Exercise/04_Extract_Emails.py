import re

data = input()

pattern = r'(?P<email>(?<=\s)([a-z0-9]+[\\.\-_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+\b)'

matches = re.finditer(pattern, data)

for match in matches:
    print(match.group('email'))