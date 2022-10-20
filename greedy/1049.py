# 기타줄
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = 0
pack = 1000 # min value
one = 1000 # min value
guitar = []

for i in range(M):
    guitar.append(list(map(int, input().split())))
    if guitar[i][0] < pack: pack = guitar[i][0]
    if guitar[i][1] < one: one = guitar[i][1]

if pack <= one * 6:
    ans = pack * (N//6) + one * (N%6)
    if pack < one * (N%6):
        ans = pack * (N//6+1)
else:
    ans = one * N

print(ans)