from collections import deque

quantity_of_food = int(input())
input_orders = input().split()
orders = deque(int(x) for x in input_orders)


print(max(orders))


while orders:
    if quantity_of_food - orders[0] < 0:
        print(f"Orders left: {' '.join(str(x) for x in orders)}")
        break
    
    quantity_of_food -= orders.popleft()

else:
    print("Orders complete")




