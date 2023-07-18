# 신입 사원
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]
    rank_asc = sorted(rank)
    answer = 1
    top = 0
    for i in range(1, N):
        if rank_asc[i][1] < rank_asc[top][1]:
            answer += 1
            top = i
    print(answer)
