import re

main_string = input()

pattern = r'([#@])(?P<word1>[A-Za-z]{3,})\1\1(?P<word2>[A-Za-z]{3,})'

list_result = list()

result = list(re.finditer(pattern, main_string))

for word in result:
    if word["word1"] == word["word2"][::-1]:
        list_result.append(f"{word['word1']} <=> {word['word2']}")

if result:
    print(f"{len(result)} word pairs found!")

    if list_result:
        print("The mirror words are:")
        print(*list_result, sep=", ")
    
    else:
        print("No mirror words!")

else:
    print("No word pairs found!")
    print("No mirror words!")
