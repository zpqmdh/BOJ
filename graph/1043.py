# 거짓말
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
truth = list(map(int, input().split()))
party = [list(map(int, input().split())) for _ in range(M)]
maps = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
answer = 0

def solve(idx):
    visited[idx] = True
    for x in maps[idx]:
        if not visited[x]:
            solve(x)
for p in party:
    for i in range(1, p[0]):
        for j in range(i+1, p[0]+1):
            maps[p[i]].append(p[j])
            maps[p[j]].append(p[i])
for i in range(1, truth[0]+1):
    solve(truth[i])
for i in range(M):
    cnt = 0
    for j in party[i][1:]:
        if not visited[j]:
            cnt += 1
    if cnt == party[i][0]:
        answer += 1

print(answer)
