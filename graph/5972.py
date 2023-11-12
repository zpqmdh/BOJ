# 택배 배송
import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
road = [[] for _ in range(N+1)] # 양방향 그래프
for _ in range(M):
    a, b, c = map(int, input().split())
    road[a].append((b, c))
    road[b].append((a, c))
result = [1e9 for _ in range(N+1)]
def solve(start):
    Q = []
    heapq.heappush(Q, (0, start))
    while Q:
        d, cur = heapq.heappop(Q)
        if result[cur] < d:
            continue
        for i in road[cur]:
            cost = d + i[1]
            if result[i[0]] > cost:
                result[i[0]] = cost
                heapq.heappush(Q, (cost, i[0]))
solve(1)
print(result[N])