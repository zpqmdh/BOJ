# 동전 1
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = [int(input().rstrip()) for _ in range(N)]
dp = [0 for _ in range(K+1)]
dp[0] = 1
for i in range(N):
    for j in range(coin[i], K+1):
        dp[j] += dp[j-coin[i]]
print(dp[K])