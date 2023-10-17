# 후위 표기식2
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
number = [-1 for _ in range(N)]
A = input().strip()
stack = []

for i in range(N):
    number[i] = int(input())
for i in A:
    if i not in '+-*/':
        stack.append(number[ord(i)-65])
    else:
        num = 0
        b = stack.pop()
        a = stack.pop()
        if i == '+':
            num = a + b
        elif i == '-':
            num = a - b
        elif i == '*':
            num = a * b
        else:
            num = a / b
        stack.append(num)
print(f'{stack[0]:.2f}')