class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []


def minimax(node, maximizing_player):

    # Leaf node
    if len(node.children) == 0:
        return node.value

    if maximizing_player:
        best = float('-inf')

        for child in node.children:
            best = max(best, minimax(child, False))

        return best

    else:
        best = float('inf')

        for child in node.children:
            best = min(best, minimax(child, True))

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

# Leaf Nodes
C.children = [Node(3), Node(5)]
D.children = [Node(6), Node(9)]
E.children = [Node(1), Node(2)]
F.children = [Node(0), Node(-1)]

result = minimax(root, True)

print("Optimal Value =", result)