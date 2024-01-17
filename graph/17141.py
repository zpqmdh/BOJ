# 연구소 2
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 1e9

virus = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])

chosen_virus = []
def make_virus(start, cnt):
    global answer
    if cnt == M:
        answer = min(answer, bfs(chosen_virus))
        return 
    for i in range(start, len(virus)):
        if virus[i] not in chosen_virus:
            chosen_virus.append(virus[i])
            make_virus(i+1, cnt+1)
            chosen_virus.pop()

def bfs(chosen_virus):
    result = 0
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    Q = deque(chosen_virus)
    for y, x in chosen_virus:
        visited[y][x] = 0

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N and board[ny][nx] != 1 and visited[ny][nx] == -1:
                Q.append([ny, nx])
                visited[ny][nx] = visited[y][x] + 1
                result = max(result, visited[ny][nx])
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and board[i][j] != 1:
                return 1e9
    return result
    
make_virus(0, 0)

if answer == 1e9:
    print(-1)
else:
    print(answer)

