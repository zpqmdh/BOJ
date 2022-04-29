# 단지번호붙이기
def dfs(y, x):
    global cnt
    cnt += 1
    visited[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_possible(ny,nx) == True and square[ny][nx] == '1' and visited[ny][nx] == False:
            dfs(ny, nx)
def is_possible(y, x):
    if y<0 or y>=N or x<0 or x>=N:
        return False
    return True
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
N = int(input())
square = []
visited = [[False] * N for _ in range(N)]
house = []
for i in range(N):
    square.append(input())

for i in range(N):
    for j in range(N):
        if square[i][j] == '1' and visited[i][j] == False:
            cnt = 0
            dfs(i, j)
            house.append(cnt)
print(len(house))
for i in sorted(house):
    print(i)