# N과 M (12)
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
        if arr[i] != before:
            ans.append(arr[i]) 
            before = arr[i]    
            dfs(i)
            ans.pop()
dfs(0)
