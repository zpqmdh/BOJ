# 연결 요소의 개수
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1

def bfs(node):
    Q = deque([])
    Q.append(node)
    visited[node] = 1
    while Q:
        n = Q.popleft()
        for i in range(1, N+1):
            if visited[i] == 0 and graph[n][i] == 1:
                Q.append(i)
                visited[i] = 1

ans = 0   
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        ans += 1
print(ans)