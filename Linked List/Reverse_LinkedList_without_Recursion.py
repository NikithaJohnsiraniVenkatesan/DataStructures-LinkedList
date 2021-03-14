#How do you reverse a singly linked list without recursion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
   
    def PrintReverse(self, temp):
        if temp:
            self.PrintReverse(temp.next)
            print(temp.data, end = " ")
        else:
            return
list1 = LinkedList()
list1.push(2)
list1.push(4)
list1.push(9)
list1.push(16)

print("The reversed linked list without recursion: ")

list1.PrintReverse(list1.head)

    