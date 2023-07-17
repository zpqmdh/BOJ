# 전자레인지
import sys
input = sys.stdin.readline

time = [300, 60, 10]
answer = [0, 0, 0]
i = 0

T = int(input())

while True:
    if T == 0:
        for a in answer:
            print(a, end=' ')
        break
    if i > 2:
        print(-1)
        break
    answer[i] = T // time[i]
    T %= time[i]
    i += 1