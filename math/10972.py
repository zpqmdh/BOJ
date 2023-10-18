# 다음 순열
import sys
input = sys.stdin.readline

N = int(input())
per = list(map(int, input().split()))
x, y = -1, -1
for i in range(N-1, 0, -1):
    if per[i] > per[i-1]:
        for j in range(N-1, 0, -1):
            if per[i-1] < per[j]:
                per[i-1], per[j] = per[j], per[i-1]
                per = per[:i] + sorted(per[i:])
                print(*per)
                exit(0)
print(-1)