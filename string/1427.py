#소트인사이드
import sys
input = sys.stdin.readline().rstrip()
arr = list(input)
print(''.join(sorted(arr, reverse=True)))