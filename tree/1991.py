# 트리 순회
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self):
        self.root = None

N = int(input())
tree = BinaryTree()
for _ in range(N):
    