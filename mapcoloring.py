# Python Program for Map Coloring using CSP (Constraint Satisfaction Problem)

# Colors available
colors = ["Red", "Green", "Blue"]

# Map of regions and their neighbors
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Dictionary to store assigned colors
color_assignment = {}

# Check if assigning a color is valid
def is_safe(region, color):
    for neighbor in graph[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

# Backtracking function
def map_coloring(region_list, index):
    
    if index == len(region_list):
        return True

    region = region_list[index]

    for color in colors:
        if is_safe(region, color):
            color_assignment[region] = color

            if map_coloring(region_list, index + 1):
                return True

            del color_assignment[region]

    return False

# Main Program
regions = list(graph.keys())

if map_coloring(regions, 0):
    print("Map Coloring Solution:")
    for region, color in color_assignment.items():
        print(region, "->", color)
else:
    print("No Solution Exists")