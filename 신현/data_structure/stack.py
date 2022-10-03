class Stack:
    def __init__(self):
        self.item_list = []
                
    def push(self,item):
        self.item_list.append(item)
        
    def pop(self) -> int:
        popped_val = self.item_list.pop()
        return popped_val
    
    def get_size(self) -> int:
        return len(self.item_list)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(5)

print(stack.pop())

print(stack.get_size())