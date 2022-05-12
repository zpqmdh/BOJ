# 토마토
import sys
from collections import deque

def bfs():
    while Q:
        z, y, x = Q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if is_possible(nz, ny, nx) == True and box[nz][ny][nx] == 0:
                Q.append([nz, ny, nx])
                box[nz][ny][nx] = box[z][y][x] + 1

def is_possible(z, y, x):
    if 0<=z<H and 0<=y<N and 0<=x<M:
        return True
    return False

Q = deque([])

dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]

input = sys.stdin.readline
M, N, H = map(int, input().split())

box = []

for i in range(H):
    tmp = []
    for j in range(N):
        tmp.append(list(map(int, input().split())))
        for k in range(M):
            if tmp[j][k] == 1:
                Q.append([i, j, k])
    box.append(tmp)

bfs()

day = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))

print(day-1)