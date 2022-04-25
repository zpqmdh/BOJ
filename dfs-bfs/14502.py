# BFS
import sys
from collections import deque
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N, M = int(sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
copy_map = map
DQ = deque([])
for i in range(N):
    for j in range(M):
        if map[i][j] == 2: # virus
            DQ.append([i, j])
def bfs():
    while DQ:
        y, x = DQ.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if copy_map[ny][nx] == 0:
                DQ.append([ny, nx])
                copy_map[ny][nx] = 2
def is_possible(i, j):
    if i<0 or i>=N or j<0 or j>=M:
        return False
bfs()