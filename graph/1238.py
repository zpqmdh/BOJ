# 파티
import sys, heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
road = [[] for _ in range(N+1)]
result = [[]]
for _ in range(M):
    a, b, c = map(int, input().split())
    road[a].append([b, c]) # a->b에 c시간 걸림

def solve(start):
    Q = []
    heapq.heappush(Q, (0, start)) # 시간, 시작노드
    distance[start] = 0
    while Q:
        d, cur = heapq.heappop(Q)
        if distance[cur] < d: # 더 탐색하지 않아도 됨
            continue
        for i in road[cur]:
            c = d + i[1]
            if c < distance[i[0]]:
                distance[i[0]] = c
                heapq.heappush(Q, (c, i[0]))
    return distance

for i in range(1, N+1):
    distance = [1e9 for _ in range(N+1)] # 시작하는 노드에 따라 거리 계산
    result.append(solve(i))

answer = []
for i in range(1, N+1):
    answer.append(result[i][X]+result[X][i])

print(max(answer))
