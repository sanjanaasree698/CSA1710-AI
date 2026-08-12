# Python Program to Implement Alpha-Beta Pruning Algorithm

import math

# Alpha-Beta Function
def alpha_beta(depth, node_index, is_max, scores, alpha, beta, max_depth):

    # Leaf node reached
    if depth == max_depth:
        return scores[node_index]

    if is_max:
        best = -math.inf

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                False,
                scores,
                alpha,
                beta,
                max_depth
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                True,
                scores,
                alpha,
                beta,
                max_depth
            )

            best = min(best, value)
            beta = min(beta, best)

            # Alpha Pruning
            if beta <= alpha:
                break

        return best

# Terminal node values
scores = [3, 5, 6, 9, 1, 2, 0, -1]

# Height of game tree
tree_depth = int(math.log2(len(scores)))

# Find optimal value
result = alpha_beta(
    0,
    0,
    True,
    scores,
    -math.inf,
    math.inf,
    tree_depth
)

print("Optimal Value:", result)