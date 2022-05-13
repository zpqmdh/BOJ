# RGB거리
import sys
N = int(sys.stdin.readline())
house = [[0, 0, 0] for _ in range(N+1)]
house[0][0] = 0
house[0][1] = 0
house[0][2] = 0
for i in range(1, N+1):
    r, g, b = map(int, sys.stdin.readline().split())
    # R
    house[i][0] = min(house[i-1][1], house[i-1][2]) + r
    # G
    house[i][1] = min(house[i-1][0], house[i-1][2]) + g
    # b
    house[i][2] = min(house[i-1][0], house[i-1][1]) + b

print(min(house[N]))
