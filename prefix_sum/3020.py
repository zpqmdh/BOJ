# 개똥벌레
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
arr = [int(input().rstrip()) for _ in range(N)]
up = [0] * (H+1)
down = [0] * (H+1)

for i in range(N):
    if i%2 == 0:
        down[arr[i]] += 1
    else:
        up[arr[i]] += 1

answer = N 
cnt = 0 

for i in range(H-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

for i in range(1, H+1):
    if answer > (down[i] + up[H-i+1]):
        answer = down[i] + up[H-i+1]
        cnt = 1
    elif answer == (down[i] + up[H-i+1]):
        cnt += 1

print(answer, cnt)