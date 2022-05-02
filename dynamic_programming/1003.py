# 피보나치 함수
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
T = int(input())
dp = [0] * 41
dp[0] = 0
dp[1] = 1
fibonacci(40)
for i in range(T):
    N = int(input())
    
    if N == 0:
        print(1, 0)
    else:
        print(dp[N-1], dp[N])
