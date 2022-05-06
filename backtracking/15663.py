# N과 M (9)
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []
visited = [False for _ in range(N)]
def dfs():
    if len(ans) == M:
        print(*ans)
        return
    before = -1
    for i in range(len(arr)):
        if visited[i] == False and before != arr[i]:
            ans.append(arr[i])
            before = arr[i]
            visited[i] = True
            dfs()
            ans.pop()
            visited[i] = False
dfs()