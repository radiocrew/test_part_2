class Node:
    def __init__(self, _value):
        self.value = _value
        self.next = None
        
    def valeu(self):
        return self.value

    def value(self, _value):
        self.value = _value

    def next(self):
        return self.next

    def next(self, _next):
        self.next = _next
    
class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.head.next = None

    def Head(self):
        return self.head

    # def add(self, _node):
    #     _node.next = self.head.next
    #     self.head.next = _node
    def add(self, _value):
        new_node = Node(_value)
    
        new_node.next = self.head.next
        self.head.next = new_node
        return

    def find(self, value):
        
        temp = self.head.next

        while temp != None:
            if temp.value == value:
                print('we found it')
                return True

            temp = temp.next

        print('we won\'t...')
        return False

    def delete(self, value):

        prev = self.head
        cur = prev.next

        while cur != None:
            if cur.value == value:
                prev.next = cur.next
                cur = None
                print('got it')
                return True

            prev = cur
            cur = prev.next

        print('we lost...')
        return False

    def clear(self):

        cur = self.head.next

        while cur != None:
            self.head.next = cur.next
            cur = None
            cur = self.head.next

        print('all cleared!')
        return

    def show(self):
        temp = self.head.next

        while temp != None:
            print(temp.value)                
            temp = temp.next

        

    def find_and_del(self, begin, value):
        prev = begin
        cur = prev.next

        while cur != None:

            if cur.value == value:
                prev.next = cur.next
                cur = None
                cur = prev.next
                continue

            prev = cur
            cur = prev.next

        return

    def delete_duplicate(self):

        cur = self.head.next

        #순회
        while cur != None:
            self.find_and_del(cur, cur.value)
            cur = cur.next

        

# linked_list =  LinkedList()

# linked_list.add(Node(1))
# linked_list.add(Node(2))
# linked_list.add(Node(3))
# linked_list.add(Node(4))
# linked_list.add(Node(2))
# linked_list.add(Node(4))
# linked_list.add(Node(3))
# linked_list.add(Node(3))
# linked_list.add(Node(30))


# linked_list.show()
# print('after del dup')

# linked_list.delete_duplicate()

# linked_list.show()

# linked_list.find(2)
# linked_list.delete(1)
# linked_list.show()

# linked_list.clear()
# linked_list.show()
