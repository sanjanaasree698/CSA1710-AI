# Python Program to Implement Minimax Algorithm for Gaming

import math

# Minimax Function
def minimax(depth, node_index, is_max, scores, max_depth):

    # Leaf node reached
    if depth == max_depth:
        return scores[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth)
        )

# Terminal node values
scores = [3, 5, 2, 9, 12, 5, 23, 23]

# Height of game tree
tree_depth = int(math.log2(len(scores)))

# Find optimal value
result = minimax(0, 0, True, scores, tree_depth)

print("Optimal Value:", result)