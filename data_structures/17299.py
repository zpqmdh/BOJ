# 오등큰수
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
F = [0 for i in range(max(A)+1)]
for i in range(N):
    F[A[i]] += 1
stack = []
result = ['' for _ in range(N)]
for i in range(N-1, -1, -1): 
    while stack and F[A[i]]>=F[stack[-1]]:
        stack.pop()
    if stack:
        result[i] = str(stack[-1])
    else:
        result[i] = '-1'
    stack.append(A[i])
    
print(' '.join(result))