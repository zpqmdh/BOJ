# N과 M (4)
N, M = map(int, input().split())
ans = []
def dfs(value):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(value, N+1):
        ans.append(i)
        dfs(i)
        ans.pop()
dfs(1)