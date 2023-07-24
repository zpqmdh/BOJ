# 숨바꼭질 3
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
INF = 1e9
visited = [INF for _ in range(200001)]

Q = deque()
visited[N] = 0
Q.append(N)

while Q:
    x = Q.popleft()
    if x == K:
        print(visited[K])
        break
    nt = x * 2 # 순간이동
    if 0 <= nt <= 200000 and visited[nt] > visited[x]:
        visited[nt] = visited[x]
        Q.appendleft(nt)
    nl = x - 1 # 좌
    nr = x + 1 # 우
    if 0 <= nl <= 200000 and visited[nl] > visited[x]+1:
        visited[nl] = visited[x] + 1
        Q.append(nl)
    if 0 <= nr <= 200000 and visited[nr] > visited[x]+1:
        visited[nr] = visited[x] + 1
        Q.append(nr)