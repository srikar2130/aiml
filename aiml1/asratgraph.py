def astar(graph, start, goal, heuristic):

    open_list = [(0, start)]
    closed_list = set()

    g = {start: 0}
    parent = {start: start}

    while open_list:

        open_list.sort()
        current = open_list.pop(0)[1]

        if current == goal:
            path = []

            while parent[current] != current:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path

        closed_list.add(current)

        for neighbor, cost in graph[current]:

            if neighbor in closed_list:
                continue

            new_g = g[current] + cost

            if neighbor not in g or new_g < g[neighbor]:

                g[neighbor] = new_g

                f = new_g + heuristic[neighbor]

                open_list.append((f, neighbor))

                parent[neighbor] = current

    return None


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1), ('D', 5)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 5), ('C', 2)]
}

heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

path = astar(graph, 'A', 'D', heuristic)

print("Path Found:", path)