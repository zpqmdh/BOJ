# 효율적인 해킹
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
com = [[] for _ in range(N+1)]
answer = []
max_com = -1
for _ in range(M):
    a, b = map(int, input().split())
    com[b].append(a)
for i in range(1, N+1):
    Q = deque()
    Q.append(i)
    visited = [False for _ in range(N+1)]
    cnt = 0
    while Q:
        cur = Q.popleft()
        visited[cur] = True
        for c in com[cur]:
            if visited[c] == False:
                visited[c] = True
                Q.append(c)
                cnt += 1
    if max_com < cnt:
        answer = [] # 초기화 후 값 추가
        answer.append(i)
        max_com = cnt
    elif max_com == cnt:
        answer.append(i)
answer.sort()
print(*answer)