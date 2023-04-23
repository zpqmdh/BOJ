# 수들의 합 2
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
def solve(start):
    value = 0
    global ans
    for i in range(start, N):
        value += A[i]
        if value == M:
            ans += 1
            return
for i in range(N):
    solve(i)
print(ans)