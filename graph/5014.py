# 스타트링크
import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
# F: 가장 높은 층, S: 현재 위치, G: 목표 위치, U: 위로 한 번에 몇층, D: 아래로 한 번에 몇층
visited = [False for _ in range(F+1)]
Q = deque()
Q.append([S, 0])
answer = 1e9

while Q:
    cur, cnt = Q.popleft()
    if cur == G:
        answer = min(answer, cnt)
        break
    for i in range(2):
        if i == 0:
            if cur+U <= F and visited[cur+U] == False:
                Q.append([cur+U, cnt+1])
                visited[cur+U] = True
        else:
            if cur-D >= 1 and visited[cur-D] == False:
                Q.append([cur-D, cnt+1])
                visited[cur-D] = True
                
if answer == 1e9:
    print("use the stairs")
else:
    print(answer)