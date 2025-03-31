def substring_calculate(first_str, second_str):
    substring = []
    for current_char1 in first_str:
        for current_char2 in second_str:
            if current_char1 in current_char2:
                substring.append(current_char1)
                break
    return substring


first_string = input().split(", ")
second_string = input().split()

print(substring_calculate(first_string, second_string))
