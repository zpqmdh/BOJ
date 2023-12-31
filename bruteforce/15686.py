# 치킨 배달
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
selected_chicken = []
answer = 99999

def solve(idx, cnt):
    if cnt == M:
        check_distance()
        return
    for i in range(idx, len(chicken)):
        selected_chicken.append(i)
        solve(i+1, cnt+1)
        selected_chicken.pop()

def check_distance():
    global answer
    result = 0
    for i in range(len(home)):
        distance = 1e5
        for j in selected_chicken:
            distance = min(distance, abs(home[i][0]-chicken[j][0])+abs(home[i][1]-chicken[j][1]))
        result += distance
    answer = min(answer, result)

for i in range(N):
    for j in range(N):
        if city[i][j] == 1: # 집
            home.append([i,j])
        if city[i][j] == 2: # 치킨집
            chicken.append([i,j])

solve(0, 0)
print(answer)
