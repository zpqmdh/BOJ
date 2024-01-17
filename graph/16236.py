# 아기 상어
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
shark_y, shark_x = 0, 0
size = 2
cnt = 0
answer = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_y, shark_x = i, j
            board[i][j] = 0

def bfs(y, x):
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[y][x] = 0 # 상어 시작 위치 0으로 초기화

    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    Q = deque()
    Q.append((y, x))
    candidate = []
    while Q:
        cur_y, cur_x = Q.popleft()
        for i in range(4):
            ny = cur_y + dy[i]
            nx = cur_x + dx[i]
            if 0<=ny<N and 0<=nx<N and visited[ny][nx] == -1:
                if board[ny][nx] <= size:
                    Q.append([ny, nx])
                    visited[ny][nx] = visited[cur_y][cur_x] + 1
                if 0 < board[ny][nx] < size:
                    candidate.append((visited[ny][nx], ny, nx))
    return sorted(candidate, key=lambda x: (x[0], x[1], x[2]))

while True:
    candidate = bfs(shark_y, shark_x)
    if len(candidate) == 0:
        print(answer)
        break
    dist, shark_y, shark_x = candidate.pop(0)
    
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
    board[shark_y][shark_x] = 0
    answer += dist
