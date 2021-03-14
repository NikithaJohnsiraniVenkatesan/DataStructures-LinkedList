#How do you reverse a linked list?

#Available solutions: Iterative method, recursive method, Simpler and Tail Recursive method, Using Stack
# All of them have time and space complexity O(n) and O(1)
#We implement iterative method here

                
class Node:
 
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
 
    def __init__(self):
        self.head = None      
        

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
 
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def printList(self):
        temp = self.head
        while(temp):
            temp1 = temp.data
            temp = temp.next
            print(temp1, temp)
            
list1 = LinkedList()
list1.push(12)
list1.push(8)
list1.push(52)
list1.push(3)

print("The given linked list: ")
list1.printList()
list1.reverse()
print("The reversed list: ")
list1.printList()