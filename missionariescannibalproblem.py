# Python Program for Missionaries and Cannibals Problem

from collections import deque

# Check if a state is valid
def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    if (m > 0 and m < c):
        return False
    if (3 - m > 0 and (3 - m) < (3 - c)):
        return False
    return True

# BFS Solution
def solve():
    start = (3, 3, 1)  # (Missionaries, Cannibals, Boat Side)
    goal = (0, 0, 0)

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        m, c, boat = state

        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for dm, dc in moves:
            if boat == 1:  # Boat on left side
                new_state = (m - dm, c - dc, 0)
            else:          # Boat on right side
                new_state = (m + dm, c + dc, 1)

            nm, nc, _ = new_state

            if is_valid(nm, nc):
                queue.append((new_state, path + [new_state]))

    return None

# Main Program
solution = solve()

if solution:
    print("Solution Path:")
    for step in solution:
        print(step)
else:
    print("No Solution Found")