# 파일 합치기 3
import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    A = list(map(int, input().split()))
    answer = 0
    heapq.heapify(A)
    while len(A) >= 2:
        a = heapq.heappop(A)
        b = heapq.heappop(A)
        answer += a+b
        heapq.heappush(A, a+b)
    print(answer)