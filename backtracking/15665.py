# N과 M (11)
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []
def dfs():
    if len(ans) == M:
        print(*ans)
        return
    before = -1
    for i in range(len(arr)):
        if before != arr[i]:
            before = arr[i]
            ans.append(arr[i])
            dfs()
            ans.pop()
dfs()