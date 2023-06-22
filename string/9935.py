# 문자열 폭발
import sys
input = sys.stdin.readline

string = input().rstrip()
bomb = input().rstrip()

stack = []
for idx in range(0, len(string)):
    s = string[idx]
    stack.append(s)
    if s == bomb[-1]:
        if ''.join(stack[-len(bomb):]) == bomb:
            for i in range(len(bomb)):
                stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))