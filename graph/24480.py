# 알고리즘 수업 - 깊이 우선 탐색 2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(R):
    global ans
    visited[R] = ans
    ans += 1
    for i in maps[R]:
        if visited[i] == 0:
            dfs(i)

N, M, R = map(int, input().split())
maps = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
ans = 1

for _ in range(M):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)
for i in range(1, N+1):
    maps[i].sort(reverse=True)

dfs(R)

for v in visited[1:]:
    print(v)