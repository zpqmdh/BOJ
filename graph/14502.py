# 연구소
import sys, copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus = []

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i, j))
            
result = 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def install_wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                install_wall(cnt + 1)
                graph[i][j] = 0

def bfs():
    global result
    Q = deque()
    for v in virus:
        Q.append(v)
    visited = [[0 for _ in range(M)] for _ in range(N)]
    while Q:
        y, x = Q.popleft()
        visited[y][x] = 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and visited[ny][nx] == 0 and graph[ny][nx] == 0:
                Q.append((ny, nx))
                visited[ny][nx] = 1
    res = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0 and visited[i][j] == 0:
                res += 1
    result = max(result, res)

install_wall(0)
print(result)