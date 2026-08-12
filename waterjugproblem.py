# Python Program for Water Jug Problem

from collections import deque

def water_jug(jug1, jug2, target):

    visited = set()
    queue = deque()

    queue.append((0, 0))
    visited.add((0, 0))

    while queue:
        x, y = queue.popleft()

        print((x, y))

        if x == target or y == target:
            print("\nTarget Reached!")
            return

        next_states = [
            (jug1, y),                  # Fill Jug1
            (x, jug2),                  # Fill Jug2
            (0, y),                     # Empty Jug1
            (x, 0),                     # Empty Jug2
            (max(0, x - (jug2 - y)),
             min(jug2, y + x)),         # Pour Jug1 -> Jug2
            (min(jug1, x + y),
             max(0, y - (jug1 - x)))    # Pour Jug2 -> Jug1
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    print("No Solution Possible")

# Main Program
jug1 = 4
jug2 = 3
target = 2

water_jug(jug1, jug2, target)