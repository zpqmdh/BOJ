# 조합
import sys
N, M = map(int, sys.stdin.readline().split())
answer = 1;
for i in range(M):
    answer *= (N-i);
for i in range(1, M+1):
    answer = answer // i;
print(answer);