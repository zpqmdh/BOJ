# 부분수열의 합
import sys
input = sys.stdin.readline
# backtracking
def dfs(sum_value, idx):
    global answer
    if len(res) > 0 and sum_value == S:
        answer += 1
        
    for i in range(idx, len(arr)):
        if visited[i] == False:
            visited[i] = True
            res.append(arr[i])
            dfs(sum(res), i+1)
            res.pop()
            visited[i] = False

N, S = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False for _ in range(N)]
res = []
answer = 0

dfs(0, 0)

print(answer)