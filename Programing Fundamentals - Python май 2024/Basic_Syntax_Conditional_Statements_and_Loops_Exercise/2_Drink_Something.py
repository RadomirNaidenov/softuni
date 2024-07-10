ages = int(input())
drink_type = ""

if ages <= 14:
    drink_type = "toddy"
elif ages <= 18:
    drink_type = "coke"
elif ages <= 21:
    drink_type = "beer"
else:
    drink_type = "whisky"

print(f"drink {drink_type}")