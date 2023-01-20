# 최댓값
import sys
input = sys.stdin.readline

board = []
max_value = -1
ans = ()

for i in range(9):
    board.append(list(map(int, input().split())))
    for idx, value in enumerate(board[i]):
        if max_value < value:
            ans = (i, idx)
            max_value = value

print(max_value)
print(ans[0]+1, ans[1]+1)