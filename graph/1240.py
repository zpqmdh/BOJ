# 노드 사이의 거리
import sys
from collections import deque
input = sys.stdin.readline
def bfs(start, end):
    Q = deque()
    Q.append((start, 0))
    visited = [False] * (N+1)
    visited[start] = True
    while Q:
        V, d = Q.popleft()
        if V == end:
            return d
        for i, dist in graph[V]:
            if visited[i] == False:
                visited[i] = True
                Q.append((i, d + dist))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    N1, N2, dist = map(int, input().split())
    graph[N1].append((N2, dist))
    graph[N2].append((N1, dist))
for _ in range(M):
    N1, N2 = map(int, input().split())
    print(bfs(N1, N2))