# 촌수계산
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
dic = {i: [] for i in range(1, N+1)}
M = int(input())

for _ in range(M):
    x, y = map(int, input().split()) # x: 부모, y: 자식
    dic[x].append(y)
    dic[y].append(x)

Q = deque()
visited = [False for _ in range(N+1)]
Q.append((a, 0)) # 사람, 촌수
visited[a] = True
answer = -1

while Q:
    cur, r = Q.popleft()
    if cur == b:
        answer = r
        break
    for person in dic[cur]:
        if not visited[person]:
            visited[person] = True
            Q.append((person, r+1))

print(answer)