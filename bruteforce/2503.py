# 숫자 야구
import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
answer = 0

for p in permutations([i for i in range(1, 10)], 3):
    flag = True
    for i in range(N):
        strike = 0
        ball = 0
        num = list(map(int, str(L[i][0])))
        for j in range(3):
            if p[j] == num[j]:
                strike += 1
            elif p[j] in num:
                ball += 1
        if strike == L[i][1] and ball == L[i][2]:
            continue
        else:
            flag = False
            break
    if flag:
        answer += 1
print(answer)