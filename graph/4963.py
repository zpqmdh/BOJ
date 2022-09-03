# 섬의 개수
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(y, x):
    # direction
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    
    visited[y][x] = 1
    
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_possible(ny, nx) and MAP[ny][nx] == 1 and visited[ny][nx] == 0:
            dfs(ny, nx)

def is_possible(y, x):
    if 0 <= y < H and 0 <= x < W:
        return True
    else:
        return False

while True:
    W, H = map(int, input().split())

    # initialize
    MAP = []
    visited = [[0 for _ in range(W)] for _ in range(H)]
    ans = 0
    
    if W == 0 and H == 0:
        break
    for _ in range(H):
        MAP.append(list(map(int, input().split())))
    for i in range(H):
        for j in range(W):
            if MAP[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                ans += 1
    print(ans)