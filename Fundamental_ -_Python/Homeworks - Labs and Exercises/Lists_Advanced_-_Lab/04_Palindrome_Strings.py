words = input().split()
palindrome_word = input()
palindromes_list = []
palindromes_count = 0
for word in words:
    if word == word[::-1]:
        palindromes_list.append(word)
    if palindrome_word == word:
        palindromes_count += 1

print(palindromes_list)
print(f"Found palindrome {palindromes_count} times")
