# 해킹
import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    dist = [1e9 for _ in range(N+1)]
    for _ in range(D):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])
    
    heap = []
    heapq.heappush(heap, [0, C])
    dist[C] = 0
    while heap:
        time, node = heapq.heappop(heap)
        for next_node, weight in graph[node]:
            if dist[next_node] > time + weight:
                heapq.heappush(heap, [time + weight, next_node])
                dist[next_node] = time + weight
    
    cnt, total = 0, 0
    for d in dist:
        if d != 1e9:
            cnt += 1
            total = max(total, d)
    print(cnt, total)