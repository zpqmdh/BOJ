# 수 찾기
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
set_A = set(A) # set 자료형 사용
M = int(input())
B = list(map(int, input().split()))
for i in range(M):
    if B[i] in set_A: # set 자료형의 in 시간 복잡도 = O(1)
        B[i] = 1
    else:
        B[i] = 0
for b in B:
    print(b)