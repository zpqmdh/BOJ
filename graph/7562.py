# 나이트의 이동
import sys
from collections import deque

input = sys.stdin.readline

def is_possible(y, x):
    global N
    if 0<=y<N and 0<=x<N:
        return True
    return False

def bfs(y, x):
    global x2, y2
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]

    Q = deque()
    Q.append((y, x))

    while Q:
        y, x = Q.popleft()
        if y == y2 and x == x2:
            return board[y2][x2]
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if is_possible(ny, nx) and board[ny][nx] == 0:
                Q.append((ny, nx)) 
                board[ny][nx] = board[y][x] + 1

T = int(input())
for _ in range(T):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print(bfs(y1, x1))
