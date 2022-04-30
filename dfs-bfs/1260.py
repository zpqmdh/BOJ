# DFS, BFS
from collections import deque
N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(node):
    visited_dfs[node] = 1
    print(node, end=' ')
    for i in range(1, N+1):
        if visited_dfs[i] == 0 and graph[node][i] == 1:
            dfs(i)

def bfs(node):
    Q = deque()
    Q.append(node)
    visited_bfs[node] = 1
    while Q:
        n = Q.popleft()
        print(n, end=' ')
        for i in range(1, N+1):
            if visited_bfs[i] == 0 and graph[n][i] == 1:
                Q.append(i)
                visited_bfs[i] = 1
                
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

dfs(V)
print()
bfs(V)