# 단어 뒤집기 2
import sys
input = sys.stdin.readline().rstrip()
ans = ""
stack = ""
flag = False
for i in input:
    if i == "<":
        flag = True
        ans += stack[::-1]
        stack = ""
        ans += i
        continue
    elif i == ">":
        flag = False
        ans += i
        continue
    elif i == " ":
        ans += stack[::-1] + " "
        stack = "" 
        continue

    if flag:
        ans += i
    else:
        stack += i
print(ans + stack[::-1])