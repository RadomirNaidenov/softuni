from collections import deque
pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_data_copy = pumps_data.copy()
petrol_in_tank = 0
index = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()
    petrol_in_tank += petrol
    if petrol_in_tank >= distance:
        petrol_in_tank -= distance
        continue
    pumps_data.rotate(-1)
    pumps_data_copy = pumps_data.copy()
    index += 1
    petrol_in_tank = 0

print(index)





