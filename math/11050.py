# 이항 계수 1
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 1
for i in range(1, K+1):
    answer *= (N-i+1)
    answer //= i
print(answer)