class Node:
    def __init__(self, data, left , right):
        self.data = data
        self.right = right
        self.left = left
    
def pre_order(node):
    print(node.data, end=" ")
    if node.left != Node:
        pre_order(node.left)    
    if node.right != Node:
        pre_order(node.right)

def in_order(node):
    if node.left != None:
        in_order(node.left)
    print(node.data, end=" ")
    if node.right != None:
        in_order(node.right)
            
def post_order(node):
    if node.left != None:
        in_order(node.left)
    if node.right != None:
        in_order(node.right)
    print(node.data, end=" ")

Node_list = []
input_list = [5,4,3,2,1]
input_Node_Name_list = ["A", "B", "C", "D", "E"]
for i in range(5):
    node = Node(input_list[i], )