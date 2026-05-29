def is_safe(vertex, graph, coloring, color):
    for neighbor in graph[vertex]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True

def graph_coloring(graph, colors, coloring, vertices, index):
    if index == len(vertices):
        return True

    vertex = vertices[index]

    for color in colors:
        if is_safe(vertex, graph, coloring, color):
            coloring[vertex] = color

            if graph_coloring(graph, colors, coloring, vertices, index + 1):
                return True

            del coloring[vertex]

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

coloring = {}
vertices = list(graph.keys())

if graph_coloring(graph, colors, coloring, vertices, 0):
    print("Solution:")
    for vertex, color in coloring.items():
        print(vertex, "->", color)
else:
    print("No solution exists")


# def is_safe(v, graph, color, c):
#     for i in range(len(graph)):
#         if graph[v][i] == 1 and color[i] == c:
#             return False
#     return True

# def graph_coloring_util(graph, m, color, v):
#     if v == len(graph):
#         return True

#     for c in range(1, m + 1):
#         if is_safe(v, graph, color, c):
#             color[v] = c

#             if graph_coloring_util(graph, m, color, v + 1):
#                 return True

#             color[v] = 0

#     return False

# def graph_coloring(graph, m):
#     n = len(graph)
#     color = [0] * n

#     if not graph_coloring_util(graph, m, color, 0):
#         print("No solution exists")
#         return False

#     print("Solution Found:")
#     for i in range(n):
#         print(f"Vertex {i} ---> Color {color[i]}")

#     return True


# graph = [
#     [0, 1, 1, 1],
#     [1, 0, 1, 0],
#     [1, 1, 0, 1],
#     [1, 0, 1, 0]
# ]

# m = 3

# graph_coloring(graph, m)