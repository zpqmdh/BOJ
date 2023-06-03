# 치킨 배달
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(N))
home = []
chicken = []
selected_chicken = []
answer = 99999

def solve(cnt):
    if cnt == M:
        check_distance()
        return
    for i in range(len(chicken)):
        if i in selected_chicken:
            continue
        selected_chicken.append(i)
        solve(cnt+1)
        selected_chicken.pop()

def check_distance():
    global answer
    distance = [987654321 for _ in range(len(home))]
    for i in range(len(home)):
        for j in selected_chicken:
            distance[i] = min(distance[i], abs(home[i][0]-chicken[j][0])+abs(home[i][1]-chicken[j][1]))
    answer = min(answer, sum(distance))

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i,j])
        if city[i][j] == 2:
            chicken.append([i,j])

solve(0)
print(answer)
