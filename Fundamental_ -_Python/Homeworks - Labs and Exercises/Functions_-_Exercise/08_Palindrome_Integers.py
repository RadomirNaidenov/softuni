def is_palindrome(some_number):
    return some_number == some_number[::-1]


numbers_as_string = input().split(", ")
for number in numbers_as_string:
    print(is_palindrome(number))