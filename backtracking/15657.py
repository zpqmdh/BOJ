# N과 M (8)
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []
def dfs(node):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(node, len(arr)):
        ans.append(arr[i])
        dfs(i)
        ans.pop()
dfs(0)