# 이진 검색 트리
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start+1, end+1):
        if pre[i] > pre[start]: # 트리를 좌우로 나누기
            mid = i
            break
    post(start+1, mid-1)
    post(mid, end)
    print(pre[start])

post(0, len(pre)-1)
