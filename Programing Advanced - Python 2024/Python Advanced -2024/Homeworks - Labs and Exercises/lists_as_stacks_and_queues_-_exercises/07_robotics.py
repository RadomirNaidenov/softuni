from collections import deque
from datetime import datetime, timedelta

robot_info = {}

for r in input().split(";"):
    robot_name, time_needed = r.split("-")
    robot_info[robot_name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")
products = deque()
product = input()

while product != "End":
    products.append(product)
    product = input()

while products:
    factory_time += timedelta(seconds=1)
    product = products.popleft()

    free_robots = []

    for name, value in robot_info.items():
        if value[1] > 0:
            robot_info[name][1] -= 1
        
        if value[1] == 0:
            free_robots.append([name, value])
    
    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robot_info[robot_name][1] = data[0]

    print(f"{robot_name} - {product} [{factory_time.strftime('%H:%M:%S')}]")

