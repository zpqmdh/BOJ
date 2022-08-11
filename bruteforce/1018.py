# 체스판 다시 칠하기
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
ans = []

for _ in range(N):
    board.append(input().rstrip())

for i in range(N-7):
    for j in range(M-7): # 8 * 8
        idx_w = 0 # board[0][0] == 'W'
        idx_b = 0 # board[0][0] == 'B
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        idx_w += 1
                    if board[k][l] != 'B':
                        idx_b += 1
                else:
                    if board[k][l] != 'B':
                        idx_w += 1
                    if board[k][l] != 'W':
                        idx_b += 1
        ans.append(idx_w)
        ans.append(idx_b)
        
print(min(ans))