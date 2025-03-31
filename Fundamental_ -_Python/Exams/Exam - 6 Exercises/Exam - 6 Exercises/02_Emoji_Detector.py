import re

piece_of_string = input().strip()
digits = ""
sum_of_all = 1
for char in piece_of_string:
    if char.isdigit():
        digits += char

for digit in digits:
    digit = int(digit)
    sum_of_all *= digit

pattern = r"(::|\*\*)(?P<word>[A-Z][a-z]{2,})\1"

matches = re.finditer(pattern, piece_of_string)
matching_lst = []
for match in matches:
    matching_lst.append(match.group())
cool_words_lst = []
for word in matching_lst:
    total_sum = 0
    for char in word[2:-2]:
        total_sum += ord(char)
    if total_sum >= sum_of_all:
            cool_words_lst.append(word)

print(f"Cool threshold: {sum_of_all}")
print(f"{len(matching_lst)} emojis found in the text. The cool ones are:")
for word in cool_words_lst:
    print(word)

    
