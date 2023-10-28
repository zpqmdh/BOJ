# 동물원
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(3)] for _ in range(N+1)]
dp[1][0] = 1 # 아무것도 두지 않음 <0 0>
dp[1][1] = 1 # 왼쪽에 둠 <1 0>
dp[1][2] = 1 # 오른쪽에 둠 <0 1>

for i in range(2, N+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901
    dp[i][2] = (dp[i-1][2] + dp[i-1][1] + dp[i-1][0]) % 9901
print(sum(dp[N])%9901)