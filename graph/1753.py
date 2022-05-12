# 최단경로
'''
> DIJKSTRA
1. 출발 노드를 설정
2. 출발 노드를 기준으로 각 노드의 최소 비용 저장
3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드 선택
4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려하여 최소 비용 갱신
5. 위 과정에서 3-4 반복
참고) 
    https://techblog-history-younghunjo1.tistory.com/247
    https://techblog-history-younghunjo1.tistory.com/248?category=1014800
'''
import sys
import heapq
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = 987654321

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1) 

def dijkstra(start):
    Q = []
    heapq.heappush(Q, (0, start)) # 
    distance[start] = 0 # start node -> start node 
    while Q:
        dist, node = heapq.heappop(Q)

        if distance[node] < dist:
            continue

        for next in graph[node]:
            cost = distance[node] + next[1] # start -> node 거리 + node -> node의 인접 노드 거리
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(Q, (cost, next[0]))
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])