# 카드 구매하기
import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))
dp = [0 for _ in range(N+1)]
for i in range(1, N+1): # 카드를 몇장 구매할거니?
    for j in range(1, i+1): # 가능한 조합 점검
        dp[i] = max(dp[i-j] + P[j-1], dp[i])
print(dp[N])
