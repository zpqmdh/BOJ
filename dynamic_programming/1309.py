# 동물원
import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
dp[0] = 1
dp[1] = 