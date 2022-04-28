# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name = [input().rstrip() for _ in range(N)]
pocketmon = {name[i]:i+1 for i in range(N)}

for j in range(M):
    input_value = input().rstrip()
    if input_value.isdigit() == True:
        input_value = int(input_value)-1
        print(name[input_value])
    else:
        print(pocketmon[input_value])