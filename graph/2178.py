# 미로 탐색
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
maze = []
visited = [[0] * (M) for _ in range(N)]
for _ in range(N):
    maze.append(sys.stdin.readline().rstrip())

def bfs():
    Q = deque([])
    Q.append([0, 0])
    visited[0][0] = 1

    while Q:
        y, x = Q.popleft()
        if y == N-1 and x == M-1:
            print(visited[y][x])
            return 
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_possible(ny, nx) == True and visited[ny][nx] == 0 and maze[ny][nx] == '1':
                Q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
    
def is_possible(y, x):
    if y<0 or y>=N or x<0 or x>=M:
        return False
    return True

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

bfs()
