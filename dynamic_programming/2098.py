# DP
import sys
N = int(input())
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
is_visit = [False] * N
def tsp():
    if is_visit[i] == False:
        