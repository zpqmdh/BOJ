# 듣보잡
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = dict()
answer = []
for _ in range(N):
    name = input().rstrip()
    arr[name] = 1 # 듣도 못한 사람
for _ in range(M):
    name = input().rstrip()
    if name in arr: # 듣도 보도 못한 사람
        answer.append(name)
answer.sort() # 정렬
print(len(answer))
print('\n'.join(answer))
