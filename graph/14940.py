# 쉬운 최단거리
import sys
from collections import deque
input = sys.stdin.readline

# 목표 지점에서 다른 지점으로 이동한다고 생각하기
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
answer = [[-1 for _ in range(M)] for _ in range(N)]
Q = deque()
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            Q.append((i, j))
            answer[i][j] = 0
        elif graph[i][j] == 0: # 원래 갈 수 없는 땅
            answer[i][j] = 0
while Q:
    y, x = Q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<N and 0<=nx<M and graph[ny][nx] == 1 and answer[ny][nx] == -1:
            answer[ny][nx] = answer[y][x] + 1
            Q.append((ny, nx))
for i in range(N):
    print(*answer[i])
