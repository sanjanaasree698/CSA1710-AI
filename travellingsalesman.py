# Python Program to Implement Travelling Salesman Problem (TSP)

from itertools import permutations

# Distance Matrix
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(graph)

# Starting city
start = 0

min_cost = float('inf')
best_path = None

# Generate all possible paths
cities = list(range(n))
cities.remove(start)

for path in permutations(cities):
    
    current_cost = 0
    current_city = start

    for city in path:
        current_cost += graph[current_city][city]
        current_city = city

    # Return to starting city
    current_cost += graph[current_city][start]

    if current_cost < min_cost:
        min_cost = current_cost
        best_path = (start,) + path + (start,)

# Display Result
print("Minimum Cost:", min_cost)
print("Optimal Path:", best_path)