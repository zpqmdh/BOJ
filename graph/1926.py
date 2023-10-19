# 그림
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
_cnt = 0
_max = 0
def solve(r, c):
    Q = deque()
    Q.append([r, c])
    size = 1
    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and maps[ny][nx]:
                visited[ny][nx] = True
                Q.append([ny, nx])
                size += 1
    return size
for i in range(N):
    for j in range(M):
        if maps[i][j] and not visited[i][j]:
            visited[i][j] = True
            _cnt += 1 # 그림 개수 증가
            _max = max(_max, solve(i, j))
print(_cnt)
print(_max)