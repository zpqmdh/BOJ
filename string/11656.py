# 접미사 배열
import sys
input = sys.stdin.readline
S = input().rstrip()
ans = []
for i in range(len(S)):
    ans.append(S[i:])
for a in sorted(ans):
    print(a)