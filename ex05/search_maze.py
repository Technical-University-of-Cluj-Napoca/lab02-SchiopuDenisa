import sys
from collections import deque

RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RESET = "\033[0m"

def read_maze(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        maze = [list(line.rstrip("\n")) for line in f]
    return maze

def find_points(maze):
    start = target = None
    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if val == "S":
                start = (r, c)
            elif val == "T":
                target = (r, c)
    if start is None or target is None:
        raise ValueError("No start or target")
    return start, target

def get_neighbors(maze, node):
    rows, cols = len(maze), len(maze[0])
    r, c = node
    neighbors = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        neighbor_r, neighbor_c = r+dr, c+dc
        if 0 <= neighbor_r < rows and 0 <= neighbor_c < cols and maze[neighbor_r][neighbor_c] != "#":
            neighbors.append((neighbor_r,neighbor_c))
    return neighbors

def bfs(maze, start, target):
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()
        if current == target:
            break
        for neighbor in get_neighbors(maze, current):
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current
    else:
        return None

    path = []
    node = target
    while node != start:
        path.append(node)
        node = came_from[node]
    path.reverse()
    return path

def dfs(maze, start, target):
    stack = [start]
    came_from = {start: None}

    while stack:
        current = stack.pop()
        if current == target:
            break
        for neighbor in get_neighbors(maze, current):
            if neighbor not in came_from:
                stack.append(neighbor)
                came_from[neighbor] = current
    else:
        return None

    path = []
    node = target
    while node != start:
        path.append(node)
        node = came_from[node]
    path.reverse()
    return path

def mark_path(maze, path):
    for row, col in path:
        if maze[row][col] not in ("S","T"):
            maze[row][col] = "*"

def print_maze(maze):
    for row in maze:
        line = ""
        for ch in row:
            if ch == "*":
                line += f"{RED}{ch}{RESET}"
            elif ch == "S":
                line += f"{YELLOW}{ch}{RESET}"
            elif ch == "T":
                line += f"{GREEN}{ch}{RESET}"
            else:
                line += ch
        print(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Not enough arguments")
        sys.exit(1)

    algorithm = sys.argv[1].lower()
    file_path = sys.argv[2]

    maze = read_maze(file_path)
    start, target = find_points(maze)

    if algorithm == "bfs":
        path = bfs(maze, start, target)
    elif algorithm == "dfs":
        path = dfs(maze, start, target)
    else:
        print("Algorithm must be 'dfs' or 'bfs'")
        sys.exit(1)

    if path is None:
        print("No path found!")
    else:
        mark_path(maze, path)
        print_maze(maze)