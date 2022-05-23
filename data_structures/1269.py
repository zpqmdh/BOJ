# 대칭 차집합
import sys
input = sys.stdin.readline
num_A, num_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
set_A = set(A + B)
set_B = set(A + B)
print(len(set_A) - num_A + len(set_B) - num_B)