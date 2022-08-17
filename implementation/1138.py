# 한 줄로 서기
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
ans = [0 for _ in range(N)]
for i in range(N):
    zero = 0
    for j in range(N):
        if zero == arr[i] and ans[j] == 0:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            zero += 1
print(*ans)