import heapq

GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))

goal_pos = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1)
}

def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                x, y = goal_pos[value]
                distance += abs(i - x) + abs(j - y)
    return distance

def get_neighbors(state):
    state = [list(row) for row in state]

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = (
                new_state[nx][ny],
                new_state[x][y]
            )

            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors

def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start))

    parent = {}
    g_cost = {start: 0}

    while pq:
        f, g, current = heapq.heappop(pq)

        if current == GOAL:
            path = []

            while current in parent:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()
            return path

        for neighbor in get_neighbors(current):
            new_g = g + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g

                h = manhattan(neighbor)
                heapq.heappush(pq, (new_g + h, new_g, neighbor))

                parent[neighbor] = current

    return None

# Example Start State
start = ((1, 2, 3),
         (4, 0, 6),
         (7, 5, 8))

solution = a_star(start)

if solution:
    print("Solution found in", len(solution) - 1, "moves\n")

    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")