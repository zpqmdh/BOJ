# 링
import sys, math
input = sys.stdin.readline
N = int(input())
R = list(map(int, input().split()))
for i in range(1, N):
    value = math.gcd(R[0], R[i])
    print(R[0]//value, '/', R[i]//value, sep='')
