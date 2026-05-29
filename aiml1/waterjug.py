from collections import deque

def water_jug_bfs(cap1, cap2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        print((x, y))

        if x == target or y == target:
            print("Goal Reached")
            return

        next_states = [
            (cap1, y),
            (x, cap2),
            (0, y),
            (x, 0),

            (x - min(x, cap2-y),
             y + min(x, cap2-y)),

            (x + min(y, cap1-x),
             y - min(y, cap1-x))
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

water_jug_bfs(4, 3, 2)