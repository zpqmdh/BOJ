# 30
import sys
input = sys.stdin.readline

N = input().rstrip()
number = []
for n in N:
    number.append(int(n))
number.sort(reverse=True)
if sum(number) % 3 == 0 and number[-1] == 0:
    for n in number:
        print(n, end='')
else:
    print(-1)