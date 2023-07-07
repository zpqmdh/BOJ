# 팰린드롬수
import sys
from collections import deque
input = sys.stdin.readline

while True:
    value = input().rstrip()
    if value == '0':
        break
    Q = deque(value)
    cmp_value = ""
    while Q:
        cmp_value += Q.pop()
    if value == cmp_value:
        print("yes")
    else:
        print("no")