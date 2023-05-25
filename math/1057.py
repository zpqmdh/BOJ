# 토너먼트
import sys
input = sys.stdin.readline
N, A, B = map(int, input().split())
answer = 0
while True:
    if A == B:
        print(answer)
        break
    A = A % 2 + A // 2
    B = B % 2 + B // 2 
    answer += 1
