from collections import deque

def main(worms, holes):
    matches = 0
    worms_length = len(worms)


    while holes and worms:
        current_hole = holes.popleft()
        current_worm = worms.pop()

        if current_hole == current_worm:
            matches += 1
            continue

        current_worm -= 3
        if current_worm <= 0:
            continue
        
        worms.append(current_worm)

    if matches:
        print(f"Matches: {matches}")
    elif not matches:
        print("There are no matches.")

    if not worms and matches == worms_length:
        print("Every worm found a suitable hole!")
    elif not worms and matches != worms_length:
        print("Worms left: none")
    elif worms:
        print(f"Worms left: {', '.join(str(x) for x in worms)}")

    if not holes:
        print("Holes left: none")
    elif holes:
        print(f"Holes left: {', '.join(str(x) for x in holes)}")

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

main(worms, holes)

