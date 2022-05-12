# 적록색약
from collections import deque

N = int(input())
area = []
visited = [[False] * N for _ in range(N)] 

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(N):
    area.append(list(input()))

def bfs(r, c):
    Q = deque([])
    Q.append([r, c])
    visited[r][c] = True
    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_possible(ny, nx) == True and visited[ny][nx] == False and area[ny][nx] == area[y][x]:
                Q.append([ny, nx])
                visited[ny][nx] = True

def is_possible(r, c):
    if r<0 or r>=N or c>=N or c<0:
        return False
    else:
        return True

ans1 = 0
ans2 = 0

# 적록색약 X
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j)
            ans1 += 1
visited = [[False] * N for _ in range(N)] # initialize
# 적록색약 O
for i in range(N):
    for j in range(N):
        if area[i][j] == 'G':
            area[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j)
            ans2 += 1
print(ans1, ans2)
