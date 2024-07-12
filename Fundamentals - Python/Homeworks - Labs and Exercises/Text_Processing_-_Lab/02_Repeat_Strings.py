sequence_of_strings = input().split(" ")
result = ""
for word in sequence_of_strings:
    length = len(word)
    result += word * length

print(result)
