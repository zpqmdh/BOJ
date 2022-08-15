# 그룹 단어 체커
import sys
input = sys.stdin.readline
N = int(input())
ans = 0
for _ in range(N):
    str = input()
    alphabet = [False for _ in range(26)]
    flag = 1
    for i in range(len(str)-1):
        if alphabet[ord(str[i])-97] == False:
            alphabet[ord(str[i])-97] = True
        elif alphabet[ord(str[i])-97] == True and str[i-1] == str[i]:
            continue
        else:
            flag = 0
            break
    if flag:
        ans += 1
print(ans)