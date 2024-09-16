numbers = tuple(input().split())
numbers_as_dict = {}

for number in numbers:
    number = float(number)
    if number not in numbers_as_dict:
        numbers_as_dict[number] = []
    numbers_as_dict[number].append(number)

for number, count in numbers_as_dict.items():
    print(f"{number} - {len(count)} times")


# "It doesn't pass in judge, but this is another option to solve this problem."
                                    # ⬇️
                                    
# numbers = tuple(input().split())
# numbers_as_dict = {}

# for number in numbers:
#     number = float(number)
#     if number not in numbers_as_dict:
#         numbers_as_dict[number] = {"count": 0}
#     numbers_as_dict[number]["count"] += 1

# for number, count in numbers_as_dict.items():
#     print(f"{number} - {count["count"]} times")