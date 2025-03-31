input_names = input().split(", ")
sorted_list = sorted(input_names, key=lambda word: (-len(word), word))
print(sorted_list)