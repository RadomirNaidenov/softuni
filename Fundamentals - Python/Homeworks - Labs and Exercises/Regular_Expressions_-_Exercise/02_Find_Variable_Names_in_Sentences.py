import re

data = input()
pattern = r'\_([A-Za-z0-9]+)'
matches = re.findall(pattern, data)

print(",".join(matches))