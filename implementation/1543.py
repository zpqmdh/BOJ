# 문서 검색
import sys
input = sys.stdin.readline

doc = input().strip()
find = input().strip()
answer = doc.split(find)
print(len(answer)-1)