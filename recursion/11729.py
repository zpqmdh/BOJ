# 하노이 탑 이동 순서
import sys
input = sys.stdin.readline

N = int(input())

def solve(N, from_pos, to_pos, aux_pos):
    if N == 1:
        print(from_pos, to_pos)
        return
    solve(N-1, from_pos, aux_pos, to_pos)
    print(from_pos, to_pos)
    solve(N-1, aux_pos, to_pos, from_pos)

print(2**N-1)
solve(N, 1, 3, 2)
