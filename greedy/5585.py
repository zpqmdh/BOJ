# 거스름돈
import sys
input = sys.stdin.readline

currency = [500, 100, 50, 10, 5, 1]
rest = 1000 - int(input())
answer = 0
i = 0

while rest:
    answer += rest // currency[i]
    rest %= currency[i]
    i += 1
    
print(answer)