# 곱셈
import sys
A, B, C = map(int, sys.stdin.readline().split())

def pow(a, b):
    if b == 1:
        return a
    else:
        x = pow(a, b//2) % C
        if b % 2 == 0:
            return x * x
        else:
            return x * x * a

print(pow(A, B) % C)