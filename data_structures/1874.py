# 스택 수열
import sys
input = sys.stdin.readline
N = int(input())
stack = []
output = []
flag = 1
cur = 1

for i in range(N):
    num = int(input())
    while cur <= num:
        stack.append('+')
        output.append(cur)
        cur += 1
    if output[-1] == num:
        stack.append('-')
        output.pop()
    else:
        flag = 0
        
if flag:
    for op in stack:
        print(op)
else:
    print("NO")