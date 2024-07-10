def is_length_valid(some_string):
    if 6 <= len(some_string) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def is_valid_pass(some_string):
    if some_string.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def have_correct_digits(some_string):
    digits_count = 0
    for char in some_string:
        if char.isdigit():
            digits_count += 1
    if digits_count >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


password = input()
is_valid = [is_length_valid(password),
            is_valid_pass(password), have_correct_digits(password)]

if all(is_valid):
    print(f"Password is valid")
