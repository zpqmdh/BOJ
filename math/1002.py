# 터렛
import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)) # 두 원의 중심 사이의 거리
    r_sum = r1 + r2
    r_dif = abs(r1 - r2)

    if d == 0: # 두 원의 중심이 일치
        if r_dif == 0: # 두 원이 일치 (r1 == r2)
            print(-1)
        else: # 두 원이 만나지 않음
            print(0)
    else:
        if r_sum == d or r_dif == d: # 외접 / 내접
            print(1)
        elif r_dif < d and d < r_sum: # 두 점에서 만남
            print(2)
        else: # 두 원이 만나지 않음
            print(0)