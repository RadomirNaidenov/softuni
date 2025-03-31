def sorted_list(numbers):

    sorted_list = []

    for number in numbers:
        sorted_list.append(number)
        sorted_list.sort()
    return sorted_list


numbers_as_strings = input().split()
number_as_digits = [int(number) for number in numbers_as_strings]

final_list = sorted_list
print(sorted_list(number_as_digits))

