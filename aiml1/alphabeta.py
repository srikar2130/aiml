class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []


def alpha_beta(node, depth, alpha, beta, maximizing):

    # Leaf node
    if len(node.children) == 0:
        return node.value

    if maximizing:

        best = float('-inf')

        for child in node.children:

            value = alpha_beta(
                child,
                depth + 1,
                alpha,
                beta,
                False
            )

            best = max(best, value)
            alpha = max(alpha, best)

            # Pruning
            if beta <= alpha:
                break

        return best

    else:

        best = float('inf')

        for child in node.children:

            value = alpha_beta(
                child,
                depth + 1,
                alpha,
                beta,
                True
            )

            best = min(best, value)
            beta = min(beta, best)

            # Pruning
            if beta <= alpha:
                break

        return best


# Create Tree

root = Node()

A = Node()
B = Node()

root.children = [A, B]

C = Node()
D = Node()
E = Node()
F = Node()

A.children = [C, D]
B.children = [E, F]

C.children = [Node(3), Node(5)]
D.children = [Node(6), Node(9)]
E.children = [Node(1), Node(2)]
F.children = [Node(0), Node(-1)]

result = alpha_beta(
    root,
    0,
    float('-inf'),
    float('inf'),
    True
)

print("Optimal Value =", result)