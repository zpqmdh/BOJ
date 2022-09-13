# 케빈 베이컨의 6단계 법칙
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    Q = deque()
    Q.append(start)
    visited = [start]
    res = [0 for _ in range(N+1)]

    while Q:
        num = Q.popleft()
        for a in friend[num]:
            if a not in visited:
                res[a] = res[num] + 1
                Q.append(a)
                visited.append(a)
    return sum(res)
    
N, M = map(int, input().split())
friend = [[] for _ in range(N+1)]
ans = []

for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(1, N+1):
    ans.append(bfs(i))

print(ans.index(min(ans)) + 1)