# 행렬 곱셈 순서
import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(1, N): # 범위
    for start in range(N):
        if start + i >= N:
            break
        dp[start][start+i] = 1e9
        for k in range(start, start+i):
            value = dp[start][k]+dp[k+1][start+i]+A[start][0]*A[k][1]*A[start+i][1]
            if value < dp[start][start+i]:
                dp[start][start+i] = value

print(dp[0][N-1])