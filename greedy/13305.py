# 주유소
import sys
input = sys.stdin.readline
N = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))
ans = 0
min_cost = 1000000001
for i in range(N-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    ans += road[i] * min_cost
print(ans)