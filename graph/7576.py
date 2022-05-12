# 토마토
import sys
from collections import deque
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

Q = deque([])

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            Q.append([i, j])
def bfs():
    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_possible(ny, nx) == True and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                Q.append([ny, nx])

def is_possible(r, c):
    if r<0 or r>=N or c>=M or c<0:
        return False
    else:
        return True

bfs()

res = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        res = max(res, box[i][j])
print(res - 1)