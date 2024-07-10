command = input()
prime_sum = 0
non_prime = 0
while command != "stop":
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue

    is_prime = True
    for divisor in range(2, current_number):
        if current_number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_sum += current_number
    else:
        non_prime += current_number

    command = input()


print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime}")

