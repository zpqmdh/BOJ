# N과 M (7)
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []
def dfs():
    if len(ans) == M:
        print(*ans)
        return
    for i in range(len(arr)):
        ans.append(arr[i])
        dfs()
        ans.pop()
dfs()