# 플로이드
import sys
def init():
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                city[i][j] = 0
            else:
                city[i][j] = INF
def floyd():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                city[i][j] = min(city[i][j], city[i][k] + city[k][j])

input = sys.stdin.readline
INF = 987654321
N = int(input())
M = int(input())
city = [[0 for _ in range(N+1)] for _ in range(N+1)]

init()
for i in range(M):
    a, b, c = map(int, input().split())
    c = min(city[a][b], c)
    city[a][b] = c
floyd()
for i in range(1, N+1):
    for j in range(1, N+1):
        if city[i][j] == INF:
            print(0, end=' ')
        else:
            print(city[i][j], end=' ')
    print()