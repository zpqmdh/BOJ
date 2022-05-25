# 스티커
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, input().split())))
    for i in range(1, N):
        if i == 1:
            sticker[0][i] += sticker[1][i-1]
            sticker[1][i] += sticker[0][i-1]
        else:
            sticker[0][i] += max(sticker[1][i-1], sticker[1][i-2])
            sticker[1][i] += max(sticker[0][i-1], sticker[0][i-2])
    print(max(sticker[0][N-1], sticker[1][N-1]))
