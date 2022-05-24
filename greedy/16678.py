# 모독
import sys
input = sys.stdin.readline
N = int(input())
honor = []
ans = 0

for _ in range(N):
    honor.append(int(input()))
honor.sort()

if honor[0] != 1:
    ans += honor[0] - 1
    honor[0] = 1

for i in range(1, N):
    if honor[i-1] < honor[i]:
        ans += honor[i] - (honor[i-1] + 1)
        honor[i] = honor[i-1] + 1
        
print(ans)