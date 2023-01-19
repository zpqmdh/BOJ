# 알고리즘 수업 - 너비 우선 탐색 1
import sys
from collections import deque
input = sys.stdin.readline

def bfs(maps, visited, R):
    global ans
    Q = deque()
    Q.append(R)
    visited[R] = ans
    while Q:
        x = Q.popleft()
        for i in maps[x]:
            if visited[i] == 0:
                Q.append(i)
                ans += 1
                visited[i] = ans
                
N, M, R = map(int, input().split())
maps = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
ans = 1

for _ in range(M):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

for i in range(1, N+1):
    maps[i].sort()

bfs(maps, visited, R)

for i in visited[1:]:
    print(i)