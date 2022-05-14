# 후위 표기식
import sys
input = list(sys.stdin.readline().rstrip())
stack = []
op = ['(', ')', '+', '-', '*', '/']
ans = ''

for i in input:
    if i not in op: # alphabet
        ans += i
    else:
        if i == '(': 
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop() # '(' 제거

        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)
            
while stack:
    ans += stack.pop()

print(ans)