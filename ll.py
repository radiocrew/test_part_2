
#재귀호출을 통한.  N번째 링크드리스트 챶기.. 

from test import Node as TNode
from test import LinkedList as TLinkedList

#...

class Counter:
    def __init__(self):
        pass

    def get_counter(self, CurNode, COUNT):

        if None == CurNode.next:
            return 1

        ret_value = self.get_counter(CurNode.next, COUNT)

        if COUNT == ret_value:
            print('you wanna :', CurNode.next.value)

        return ret_value + 1


linked_list = TLinkedList()


linked_list.add(10)
linked_list.add(20)
linked_list.add(30)
linked_list.add(40)


counter = Counter()

counter.get_counter(linked_list.head, 2)

#4-3-2-1 
#뒤에서 2번째 : 2






    