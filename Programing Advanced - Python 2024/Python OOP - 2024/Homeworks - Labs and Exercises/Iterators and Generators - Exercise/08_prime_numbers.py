def get_primes(some_list: list):
    for num in some_list:
        if num <= 1:
            continue
        for divisor in range(2, num):
            if num % divisor == 0:
                break
        else:
            yield num


