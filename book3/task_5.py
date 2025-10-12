class Stack:
    def __init__(self) -> None:
        self.__items = []

    def push(self,item):
        self.__items.append(item)
    
    def pop(self):
        return self.__items.pop()
    
    def is_empty(self):
        return not bool(self.__items)
    
    def size(self):
        return len(self.__items)
    
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())
print(stack.pop())

print(stack.is_empty())

print(stack.size())

# print(stack.__items)