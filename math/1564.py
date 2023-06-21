# 팩토리얼5
import sys
input = sys.stdin.readline

N = int(input())
ans = 1
for i in range(2, N+1):
    ans *= i
    while str(ans)[-1] == '0':
        ans //= 10
    ans = int(str(ans)[-15:])
print(str(ans)[-5:])
    