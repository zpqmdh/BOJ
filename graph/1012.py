# 유기농 배추
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(r, c):
    Q = deque([])
    Q.append([r, c])
    visited[r][c] = True

    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_possible(ny, nx) == True and field[ny][nx] == 1 and visited[ny][nx] == False:
                Q.append([ny, nx])
                visited[ny][nx] = True

def is_possible(r, c):
    if r<0 or r>=N or c>=M or c<0:
        return False
    else:
        return True

T = int(input())
for i in range(T):
    ans = 0 # 필요한 배추흰지렁이 수
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for j in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    
    for a in range(N):
        for b in range(M):
            if field[a][b] == 1 and visited[a][b] == False:
                ans += 1
                bfs(a, b)
    print(ans)