# 최소비용 구하기
import sys, heapq
input = sys.stdin.readline
INF = 987654321

N = int(input())
M = int(input())

city = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start))
    distance[start] = 0
    while Q:
        dist, node = heapq.heappop(Q)

        if distance[node] < dist:
            continue
        
        for next in city[node]:
            cost = distance[node] + next[1] 
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(Q, (cost, next[0]))

for i in range(M):
    a, b, c = map(int, input().split())
    city[a].append((b, c))

start, end = map(int, input().split())

dijkstra(start)
print(distance[end])