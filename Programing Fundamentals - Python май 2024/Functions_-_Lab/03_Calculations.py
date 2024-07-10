def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a // b


def multiply(a, b):
    return a * b


def calculate():
    operator = input()
    num1 = int(input())
    num2 = int(input())
    result = 0
    if operator == "add":
        result = add(num1, num2)
    elif operator == "subtract":
        result = subtract(num1, num2)
    elif operator == "divide":
        result = divide(num1, num2)
    elif operator == "multiply":
        result = multiply(num1, num2)

    print(result)


calculate()



