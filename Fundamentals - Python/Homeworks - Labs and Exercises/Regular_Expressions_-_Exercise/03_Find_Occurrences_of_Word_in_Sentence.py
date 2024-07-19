import re

data = input()
data_to_search = input()
pattern = fr"\b{data_to_search}\b"

matches = re.findall(pattern, data, re.IGNORECASE)

print(len(matches))