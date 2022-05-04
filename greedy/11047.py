# 동전 0
import sys
N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
coin.sort(reverse=True)
res = 0
for i in range(N):
    res += K // coin[i]
    K = K % coin[i]
print(res)