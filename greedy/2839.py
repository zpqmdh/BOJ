# 설탕 배달
import sys
input = sys.stdin.readline
N = int(input())
flag = 0
answer = 0
while N >= 0:
    if N % 5 == 0:
        answer += N // 5
        print(answer)
        flag = 1
        break
    N -= 3
    answer += 1
if flag == 0:
    print(-1)
