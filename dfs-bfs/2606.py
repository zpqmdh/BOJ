# 바이러스
import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

computer = [[0] * N for _ in range(N)]
virus = [False] * N

def dfs(n):
    virus[n] = True
    for i in range(N):
        if computer[n][i] == 1 and virus[i] == False:
            dfs(i)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    computer[a-1][b-1] = 1
    computer[b-1][a-1] = 1
    
dfs(0) # 1번 컴퓨터 바이러스

ans = 0
for i in range(N):
    if virus[i] == True:
        ans += 1
print(ans - 1) # 1번 컴퓨터 제외
