from collections import deque

def main(contestants, pies):

    while contestants and pies:
        current_contestant = contestants.popleft()
        current_pie = pies.pop()

        if current_contestant >= current_pie:
            current_contestant -= current_pie            
            if current_contestant > 0:
                contestants.append(current_contestant)
        
        elif current_contestant < current_pie:
            current_pie -= current_contestant
            if current_pie == 1 and pies:
                pies[-1] += current_pie
            elif current_pie != 1 or current_pie > 0:
                pies.append(current_pie)
            
    if not pies and contestants:
        print("We will have to wait for more pies to be baked!")
        print(f"Contestants left: {', '.join(str(x) for x in contestants)}")          

    if not pies and not contestants:
        print("We have a champion!")
    
    if not contestants and pies:
        print("Our contestants need to rest!")
        print(f"Pies left: {', '.join(str(x) for x in pies)}")


contestants = deque([int(x) for x in input().split()])
pies = [int(x) for x in input().split()]

main(contestants, pies)

