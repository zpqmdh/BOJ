# N과 M (6)
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = []
arr.sort()
def dfs(node):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(node, len(arr)):
        if arr[i] not in ans:
            ans.append(arr[i])
            dfs(i)
            ans.pop()
dfs(0)
