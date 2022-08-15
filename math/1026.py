# 보물
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += sorted(A)[i] * sorted(B, reverse=True)[i]
print(ans)