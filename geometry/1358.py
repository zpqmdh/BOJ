# 하키
import sys
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())
R1 = [X, Y+H//2]
R2 = [X+W, Y+H//2]

answer = 0
for i in range(P):
    player = list(map(int, input().split()))
    if X<=player[0]<=X+W and Y<=player[1]<=Y+H:
        answer += 1
    elif (player[0]-R1[0])**2 + (player[1]-R1[1])**2 <= (H//2)**2:
        answer += 1
    elif (player[0]-R2[0])**2 + (player[1]-R2[1])**2 <= (H//2)**2:
        answer += 1
print(answer)