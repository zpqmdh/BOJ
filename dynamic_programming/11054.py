# 가장 긴 바이토닉 부분 수열
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
r_A = A[::-1]
i_dp = [0 for _ in range(N)]
d_dp = [0 for _ in range(N)]
answer = [0 for _ in range(N)]

for i in range(N):
    i_dp[i] = 1
    d_dp[i] = 1
    for j in range(i):
        if A[i] > A[j]:
            i_dp[i] = max(i_dp[i], i_dp[j]+1)
        if r_A[i] > r_A[j]:
            d_dp[i] = max(d_dp[i], d_dp[j]+1)

for i in range(N):
    answer[i] = i_dp[i] + d_dp[N-i-1] - 1

print(max(answer))
