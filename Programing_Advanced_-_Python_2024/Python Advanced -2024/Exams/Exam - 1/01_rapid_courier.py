from collections import deque

packages = list(map(int, input().split()))
couriers = list(map(int, input().split()))

package_queue = deque(packages)
courier_queue = deque(couriers)

total_delivered_weight = 0

while package_queue and courier_queue:
    package_weight = package_queue.pop()
    courier_capacity = courier_queue.popleft()
    
    if courier_capacity >= package_weight:
        total_delivered_weight += package_weight
        if courier_capacity > package_weight:
            new_capacity = courier_capacity - 2 * package_weight
            if new_capacity > 0:
                courier_queue.append(new_capacity)
    else:
        remaining_weight = package_weight - courier_capacity
        total_delivered_weight += courier_capacity
        if remaining_weight > 0:
            package_queue.appendleft(remaining_weight)

print(f"Total weight: {total_delivered_weight} kg")

if not package_queue and not courier_queue:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif not courier_queue:
    remaining_packages = ', '.join(map(str, package_queue))
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {remaining_packages}")
else:
    remaining_couriers = ', '.join(map(str, courier_queue))
    print(f"Couriers are still on duty: {remaining_couriers} but there are no more packages to deliver.")

