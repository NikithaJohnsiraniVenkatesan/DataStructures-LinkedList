#How do you check if a given linked list contains a cycle? How do you find the starting node of the cycle? 

#One solution is Hashing approach but time complexity is O(n) and auxilary space complexity is O(n)
#Three solutions 
#1. Modify the linked list data strcuture (A flag visit each node, if flag sees visited node again, there is loop)
#2. Floyd's cycle Finding Algorithm (Two pointers slow and fast, slow pointer moves by one and fast pointer moves by 2.
#                                     If these pointers meet at same node, there is loop)
#3. Marking visiting nides without modifying the data structure (Temp node is created.)
# All three methods have time O(n) and space O(1)
# We are going to implement Floyd's cyce method


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
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, temp = temp.next)
    def DetectLoop(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while(slow_pointer and fast_pointer and fast_pointer.next):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return

list1 = LinkedList()
list1.push(20)
list1.push(4)
list1.push(15)
list1.push(10)

list1.head.next.next.next.next = list1.head
if(list1.DetectLoop()):
    print("Loop is found in the linked list")
else:
    print("There is no loop")
        