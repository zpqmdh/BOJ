# 분수찾기
import sys
input = sys.stdin.readline

X = int(input())
line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0: # 짝수 줄에는 분자가 오름차순 분모가 내림차순
    a = X
    b = line - X + 1
else: # 홀수 줄에는 분자가 내림차순 분모가 오름차순
    a = line - X + 1
    b = X
print(a, '/', b, sep='')
