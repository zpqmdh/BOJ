# 알파벳
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
for i in range(R):
    board.append(list(map(lambda k: ord(k)-65, input().strip())))
visited = [False for _ in range(26)]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
answer = 0

def dfs(y, x, cnt):
    global answer
    visited[board[y][x]] = True
    answer = max(answer, cnt)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<R and 0<=nx<C:
            if visited[board[ny][nx]] == False:
                visited[board[ny][nx]] = True
                dfs(ny, nx, cnt+1)
                visited[board[ny][nx]] = False

dfs(0,0,1)
print(answer)
