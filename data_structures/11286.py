# 절댓값 힙
import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print("0")
    else:
        heapq.heappush(heap, (abs(X), X)) # (X의 절댓값, X)