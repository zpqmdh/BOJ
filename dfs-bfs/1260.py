# DFS, BFS
N, M, V = map(int, input().split())
map = [[0] * N] * N
for i in range(M):
    a, b = map(int, input().split())
    map[a][b] = 1
    map[b][a] = 1
dfs_ans = []
bfs_ans = []
def dfs(node):
    for i in range(N):
        if i not in dfs_ans and map[node][i] == 1: # 연결 되어 있다면
            dfs_ans += i
            dfs(i)
dfs(V)
print(dfs_ans)