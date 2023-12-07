# 결혼식
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
answer = 0
friends = [list() for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)
Q = deque()
Q.append((1, 0))
visited[1] = True # 상근이 방문 체크
while Q:
    cur, depth = Q.popleft()
    if 1 <= depth <= 2: # 친구 or 친구의 친구
        answer += 1
    for next in friends[cur]:
        if not visited[next]:
            Q.append((next, depth+1))
            visited[next] = True
print(answer)