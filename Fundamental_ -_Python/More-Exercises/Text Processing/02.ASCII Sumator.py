first_char = input().strip()
second_char = input().strip()
random_string = input().strip()

first_ascii = ord(first_char)
second_ascii = ord(second_char)

if first_ascii > second_ascii:
    first_ascii, second_ascii = second_ascii, first_ascii


total_sum = sum(ord(char) for char in random_string if first_ascii < ord(char) < second_ascii)


print(total_sum)
