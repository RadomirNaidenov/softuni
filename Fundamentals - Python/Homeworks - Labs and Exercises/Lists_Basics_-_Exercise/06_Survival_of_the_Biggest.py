list_of_strings = input().split()
removing_numbers_count = int(input())
integer_list = []

for number in list_of_strings:
    integer_list.append(int(number))

for remove_num in range(removing_numbers_count):
    min_number = min(integer_list)
    integer_list.remove(min_number)

print(", ".join(str(current_element) for current_element in integer_list))









