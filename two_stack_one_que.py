

#https://www.youtube.com/watch?v=t45d7CgDaDM


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        pass

    def next(self):
        return self.next

    def next(self, data):
        self.data = data

class Stack:
    def __init__(self):
        self.top = None
        pass

    def push(self, data):

        new_node = Node(data)

        if None == self.top:
            self.top = new_node
            new_node.next = None
        else:
            new_node.next = self.top
            self.top = new_node

        pass

    def pop(self):
        
        if None == self.top:
            return

        if None != self.top.next:
            self.top = self.top.next
            return

        self.top = None
        pass

    def peek(self):
        return self.top.data

    def is_empty(self):
        if None == self.top:
            return True

        return False


stack = Stack()





