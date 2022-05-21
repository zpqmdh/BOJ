# 잃어버린 괄호
import sys
input = sys.stdin.readline().split('-')
number = []
for i in input:
    cnt = 0
    tmp = i.split('+')
    for j in tmp:
        cnt += int(j)
    number.append(cnt)
ans = number[0]
for i in range(1, len(number)):
    ans -= number[i]
print(ans)