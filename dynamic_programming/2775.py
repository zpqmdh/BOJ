# 부녀회장이 될테야
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    K = int(input())
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    for i in range(1, K+1):
        dp[0][i] = i
    for i in range(1, N+1):
        for j in range(1, K+1):
            dp[i][j] = sum(dp[i-1][1:j+1])
    print(dp[N][K])