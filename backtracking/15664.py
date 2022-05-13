# N과 M (10)
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []
visited = [False for _ in range(N)]
def dfs(node):
    if len(ans) == M:
        print(*ans)
        return 
    before = -1
    for i in range(node, len(arr)):
        if visited[i] == False and before != arr[i]:
            before = arr[i]
            ans.append(arr[i])
            visited[i] = True
            dfs(i)
            ans.pop()
            visited[i] = False
dfs(0)