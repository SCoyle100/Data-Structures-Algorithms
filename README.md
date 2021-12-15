# Data-Structures-Algorithms
//Doubly Linked List Practice

class DoublyLinkedList:
  def__init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1


    my_doubly_linked_list = DoublyLinkedList(7)