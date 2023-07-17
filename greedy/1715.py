# 카드 정렬하기
import sys
from heapq import *
input = sys.stdin.readline

N = int(input())
A = [int(input()) for _ in range(N)]
heapify(A)
answer = 0

while True:
    if len(A) == 1:
        print(A)
        print(answer)
        break
    a = heappop(A)
    b = heappop(A)
    value = a+b
    heappush(A, value)
    answer += value