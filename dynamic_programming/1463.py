# 1로 만들기
N = int(input())
dp = [0] * (N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1] + 1 # 3
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) # 2
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1) # 1
print(dp[N])