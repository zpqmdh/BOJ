# 분수 합
import sys, math
input = sys.stdin.readline

n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

fn, fd = n1*d2 + n2*d1, d1*d2
print(fn//math.gcd(fn, fd), fd//math.gcd(fn, fd))