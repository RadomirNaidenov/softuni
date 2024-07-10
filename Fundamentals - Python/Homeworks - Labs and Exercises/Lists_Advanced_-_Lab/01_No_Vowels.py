input_word = input()
vowels = 'a', 'o', 'u', 'e', 'i', "A", "O", "U", "E", "I"
new_text = "".join([word for word in input_word if word not in vowels])
print(new_text)