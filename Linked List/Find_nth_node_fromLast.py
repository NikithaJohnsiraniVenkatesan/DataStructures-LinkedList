#How do you find the third node from the end in a singly linked list?
#2 solutions: double pointer concept (calculate the length of the linked list and print the length-n+1 node)

class node:
    def __init__(self, data ):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def PrintNth(self, n):
        temp = self.head
        length = 0
        while temp is not None:
            temp = temp.next
            length += 1
        if n>length:
            print("Location is greater than the length of the linked list")
            return
        temp = self.head
        for i in range(0, length-n):
            temp = temp.next
        print(temp.data)

list1 = LinkedList()
list1.push(2)
list1.push(7)
list1.push(5)
list1.push(6)
list1.push(8)

list1.PrintNth(4)
        