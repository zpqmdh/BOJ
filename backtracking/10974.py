# 모든 순열
import sys
input = sys.stdin.readline
# backtracking
def dfs(n):
    if n == N:
        print(*res)
    for i in range(N):
        if not visited[i]: # not visited
            visited[i] = True
            res.append(i+1)
            dfs(n+1)
            res.pop()
            visited[i] = False

N = int(input())
res = [] # sequence
visited = [False for _ in range(N)] # avoid duplication
dfs(0)