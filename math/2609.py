# 최대공약수와 최소공배수
import math
N, M = map(int, input().split())
print(math.gcd(N, M))
print(math.lcm(N, M))