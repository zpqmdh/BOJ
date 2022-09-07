# 영역 구하기
import sys
from collections import deque

input = sys.stdin.readline

def is_possible(y, x):
    global M, N
    if 0<=y<M and 0<=x<N:
        return True
    return False

def bfs(y, x):
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    Q = deque()
    Q.append((y, x))
    visited[y][x] = True
    res = 0
    while Q:
        y, x = Q.popleft()
        res += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_possible(ny, nx) and paper[ny][nx] == 0 and visited[ny][nx] == False:
                Q.append((ny, nx))
                visited[ny][nx] = True
    return res

M, N, K = map(int, input().split())
paper = [[0 for _ in range(N)] for _ in range(M)]
visited = [[False for _ in range(N)] for _ in range(M)]
ans = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(M-y2, M-y1):
        for j in range(x1, x2):
            paper[i][j] = 1

for i in range(M):
    for j in range(N):
        if paper[i][j] == 0 and visited[i][j] == False:
            ans.append(bfs(i, j))
            
print(len(ans))
print(*sorted(ans))