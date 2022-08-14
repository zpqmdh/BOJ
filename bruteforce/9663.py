def n_queens(rowPos):
    global ans
    
    if rowPos == N:
        ans += 1
        return
    
    for col in range(N):
        flag = True
        for row in range(rowPos):
            # 같은 열에 위치해있거나 대각선에 퀸이 이미 존재한다면
            if board[row] == col or rowPos - row == abs(col - board[row]):
                flag = False
                break
        if flag:
            board[rowPos] = col
            n_queens(rowPos + 1)
    
N = int(input())
ans = 0
board = [0] * N
n_queens(0)
print(ans)