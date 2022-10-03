import sys
from turtle import right
input = sys.stdin.readline

class Node:
    def __init__(self, name, left,right):
        self.name = name
        self.left = left
        self.right = right
    
N = int(input())
root = ""
tree = {}
for i in range(N):
    name, left, right = input().strip().split()
    tree[name] = Node(name, left, right)
    if(i == 0):
        root = name    
        
def pre_order(node):
    print(node.name, end=" ")
    if(node.left != "."):
        pre_order(tree[node.left])
    if(node.right != "."):
        pre_order(tree[node.right])

print(tree[root].name)
pre_order(tree[root]) 
