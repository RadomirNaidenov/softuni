def next_version(some_num):
    some_num = int(''.join(some_num)) + 1
    return ".".join(str(some_num))


number = input().split(".")
result = (next_version(number))
print(result)