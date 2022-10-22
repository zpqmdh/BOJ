# 괄호
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
	PS = input()
	stack = []
	for i in PS:
		if i == "(":
			stack.append(i)
		elif i == ")":
			if stack:
				stack.pop()
			else:
				print("NO")
				break
		else:
			if stack:
				print("NO")
			else:
				print("YES")