n = int(input())
negative_list = []
positive_list = []
sum_of_negative_numbers = 0
positive_counter = 0

for _ in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)
        positive_counter += 1

    elif current_number < 0:
        negative_list.append(current_number)
        sum_of_negative_numbers += current_number

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_counter}")
print(f"Sum of negatives: {sum_of_negative_numbers}")
