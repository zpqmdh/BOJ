# 경로 찾기
import sys
from collections import deque
input = sys.stdin.readline

def floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                adj[i][j] = min(adj[i][j] , adj[i][k] + adj[k][j])

adj = []
N = int(input())
INF = 987654321
for i in range(N):
    adj.append(list(map(int, input().split())))
    for j in range(N):
        if adj[i][j] == 0:
            adj[i][j] = INF
floyd()
for i in range(N):
    for j in range(N):
        if adj[i][j] == INF:
            adj[i][j] = 0
        else:
            adj[i][j] = 1
for i in range(N):
    print(*adj[i])