def add_numbers(some_numbers: list, some_negative_numbers: list, some_positive_numbers: list) -> list:
    for num in some_numbers:
        if num < 0:
            some_negative_numbers.append(num)
            continue
        some_positive_numbers.append(num)
    
    return some_negative_numbers, some_positive_numbers

numbers = list(map(int, input().split()))
negative_numbers = []
positive_numbers = []
negative_numbers, positive_numbers = add_numbers(numbers, negative_numbers, positive_numbers)

sum_negative_numbers = sum(negative_numbers)
sum_positive_numbers = sum(positive_numbers)


print(sum_negative_numbers)
print(sum_positive_numbers)

print("The negatives are stronger than the positives" if abs(sum_negative_numbers) > sum_positive_numbers else "The positives are stronger than the negatives")