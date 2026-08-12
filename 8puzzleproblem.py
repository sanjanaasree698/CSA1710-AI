# Python Program to Solve the 8-Puzzle Problem using BFS

from collections import deque

# Goal State
goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

# Possible moves of blank tile
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        visited.add(tuple(state))

        blank = state.index(0)

        for move in moves[blank]:
            new_state = state[:]
            new_state[blank], new_state[move] = new_state[move], new_state[blank]

            if tuple(new_state) not in visited:
                queue.append((new_state, path + [state]))

    return None

# Initial State
start = [1, 2, 3,
         4, 5, 6,
         0, 7, 8]

solution = bfs(start)

if solution:
    print("Solution Found:")
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No Solution Exists")