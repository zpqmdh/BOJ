# 정수 삼각형
import sys
input = sys.stdin.readline

N = int(input())
triangle = []
for _ in range(N):
    triangle.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i])-1:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
            
print(max(triangle[-1]))