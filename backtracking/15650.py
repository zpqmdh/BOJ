# backtracking
N, M = map(int, input().split())
ans = []
def dfs(n):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(n, N+1):
        if i not in ans:
            ans.append(i)
            dfs(i)
            ans.pop()
dfs(1)