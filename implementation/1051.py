# 숫자 정사각형
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
square = []
for _ in range(N):
    square.append(list(input()))

side = min(N, M) 
ans = 0

for i in range(N):
    for j in range(M):
        for k in range(side):
            if i+k < N and j+k < M and square[i][j] == square[i+k][j] == square[i][j+k] == square[i+k][j+k]:
                ans = max(ans, (k+1) ** 2)
print(ans)