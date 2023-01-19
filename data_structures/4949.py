# 균형잡힌 세상
import sys
input = sys.stdin.readline

while True:
    stack = []
    input_string = input().rstrip()
    flag = True # 문자열이 올바른지 판단하기 위한 값
    if input_string == '.':
        break
    for i in input_string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0:
                flag = False
                break
            c = stack.pop()
            if c != '(':
                flag = False
                break
        elif i == ']':
            if len(stack) == 0:
                flag = False
                break
            c = stack.pop()
            if c != '[':
                flag = False
                break
    if len(stack) != 0:
        flag = False

    if flag:
        print("yes")
    else:
        print("no")