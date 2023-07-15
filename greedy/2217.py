# 로프
import sys
input = sys.stdin.readline

N = int(input())
rope = [int(input()) for _ in range(N)]
rope.sort(reverse=True)

for i in range(N):
    rope[i] *= (i+1)
    
print(max(rope))