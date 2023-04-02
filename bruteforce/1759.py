# 암호 만들기
import sys
input = sys.stdin.readline
L, C = map(int, input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
chs = sorted(list(input().split())) # sort
visited = [False for _ in range(C)]
password = []
chk = [0, 0] # 자음의 개수, 모음의 개수
def solve(idx, cnt):
    global chk
    if cnt == L:
        # check
        for v in vowels:
            if v in password:
                chk[1] += 1
        chk[0] = len(password) - chk[1]
        if chk[0] >= 2 and chk[1] >= 1:
            print(''.join(password))
        chk = [0, 0] # initialize
        return
    for i in range(idx, C):
        if visited[i] == False:
            password.append(chs[i])
            visited[i] = True
            solve(i, cnt+1)
            password.pop()
            visited[i] = False
solve(0, 0)
