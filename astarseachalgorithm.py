# Python Program to Implement A* Search Algorithm

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 4},
    'E': {'G': 2},
    'F': {'G': 1},
    'G': {}
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}

def a_star(start, goal):
    open_list = [(start, 0)]
    closed_list = set()
    parent = {start: None}
    cost = {start: 0}

    while open_list:
        open_list.sort(key=lambda x: cost[x[0]] + heuristic[x[0]])
        current = open_list.pop(0)[0]

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        closed_list.add(current)

        for neighbor, weight in graph[current].items():
            new_cost = cost[current] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current

                if neighbor not in closed_list:
                    open_list.append((neighbor, new_cost))

    return None

# Main Program
path = a_star('A', 'G')

print("Shortest Path:")
print(" -> ".join(path))