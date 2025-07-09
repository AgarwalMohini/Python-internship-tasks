#Maze generator and solver

import random
from collections import deque

N = int(input("Enter maze size (odd number recommended, e.g., 11): "))

if N % 2 == 0:
    N += 1
    print(f"Adjusted size to odd number: {N}")

def init_maze(N):
    return [[0 for _ in range(N)] for _ in range(N)]

def carve_passages(x, y, maze):
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 < nx < N and 0 < ny < N and maze[ny][nx] == 0:
            maze[ny - dy // 2][nx - dx // 2] = 1 
            maze[ny][nx] = 1  
            carve_passages(nx, ny, maze)

def solve_maze(maze):
    visited = [[False] * N for _ in range(N)]
    prev = [[None] * N for _ in range(N)]
    queue = deque()

    start = (1, 1)
    end = (N - 2, N - 2)

    queue.append(start)
    visited[start[1]][start[0]] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if maze[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    prev[ny][nx] = (x, y)
                    queue.append((nx, ny))

    x, y = end
    while prev[y][x]:
        maze[y][x] = 2
        x, y = prev[y][x]
    maze[start[1]][start[0]] = 2

def print_maze(maze):
    for y in range(N):
        line = ""
        for x in range(N):
            if (x, y) == (1, 1):
                line += "S"
            elif (x, y) == (N - 2, N - 2):
                line += "E"
            elif maze[y][x] == 0:
                line += "#"
            elif maze[y][x] == 1:
                line += "."
            elif maze[y][x] == 2:
                line += "*"
        print(line)

maze = init_maze(N)
maze[1][1] = 1  
carve_passages(1, 1, maze)

solve_maze(maze)
print_maze(maze)
