def loading_bar(some_number) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percent_as_digit = some_number // 10
    return f"{some_number}% [{'%' * loaded_percent_as_digit}{'.' * (10 - loaded_percent_as_digit)}]\nStill loading..."


integer_number = int(input())
print(loading_bar(integer_number))