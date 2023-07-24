# 녹색 옷 입은 애가 젤다지?
import sys
from collections import deque
input = sys.stdin.readline

cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    A = [list(map(int, input().split())) for _ in range(N)]
    INF = 1e9
    visited = [[INF for _ in range(N)] for _ in range(N)]
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    def move(y, x):
        Q = deque()
        Q.append((y, x))
        visited[y][x] = A[y][x] # 방문처리
        while Q:
            r, c = Q.popleft()
            for i in range(4):
                nr = r + dy[i]
                nc = c + dx[i]
                if 0<=nr<=N-1 and 0<=nc<=N-1: # 범위 내
                    if visited[nr][nc] > visited[r][c]+A[nr][nc]:
                        visited[nr][nc] = visited[r][c]+A[nr][nc]
                        Q.append((nr, nc))

    move(0, 0)
    answer = visited[N-1][N-1]
    
    print(f"Problem {cnt}: {answer}")
    cnt += 1