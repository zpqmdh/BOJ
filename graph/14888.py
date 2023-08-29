# 연산자 끼워넣기
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
max_value = -1e9 + 1
min_value = 1e9 + 1
def solve(cnt, res):
    global max_value, min_value
    if cnt == N:
        max_value = max(max_value, res)
        min_value = min(min_value, res)
        return
    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            if i == 0: # add
                solve(cnt+1, res + A[cnt])
            elif i == 1: # sub
                solve(cnt+1, res - A[cnt])
            elif i == 2: # mul
                solve(cnt+1, res * A[cnt])
            elif i == 3: # div
                if res < 0: # if res is negative
                    solve(cnt+1, -1*(abs(res) // A[cnt]))
                else: # if res is positive
                    solve(cnt+1, res // A[cnt])
            op[i] += 1 
solve(1, A[0])
print(max_value)
print(min_value)