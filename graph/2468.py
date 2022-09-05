# 안전 영역
import sys
from collections import deque
input = sys.stdin.readline

def is_possible(y, x):
    if y<0 or y>=N or x<0 or x>=N:
        return False
    return True

def bfs(y, x, height, visited):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    Q = deque()
    Q.append((y, x))
    visited[y][x] = True
    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_possible(ny, nx) and graph[ny][nx] > height and visited[ny][nx] == False:
                Q.append((ny, nx))
                visited[ny][nx] = True

N = int(input())
graph = []
res = 0
max_num = 0

for i in range(N):
    graph.append(list(map(int, input().split())))
    if max(graph[i]) > max_num:
        max_num = max(graph[i])

for i in range(max_num):
    visited = [[False for _ in range(N)] for _ in range(N)]
    ans = 0
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == False:
                bfs(j, k, i, visited)
                ans += 1
    if res < ans:
        res = ans
print(res)