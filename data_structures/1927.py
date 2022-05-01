# 최소 힙
import sys
import heapq
N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    X = int(sys.stdin.readline())
    if X == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print("0")
    else:
        heapq.heappush(heap, X)