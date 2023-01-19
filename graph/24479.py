# 알고리즘 수업 - 깊이 우선 탐색 1
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(visited, maps, R):
    global ans
    visited[R] = ans
    ans += 1
    for i in maps[R]:
        if visited[i] == 0:
            dfs(visited, maps, i)

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
dfs(visited, maps, R)

for a in visited[1:]:
    print(a)
