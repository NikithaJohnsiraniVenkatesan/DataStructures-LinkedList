#How are duplicate nodes removed in an unsorted linked list?

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
    def RemoveDuplicates(self, head):
        if self.head is None or self.head.next is None:
            return head
        hash = set()
        current = head
        hash.add(self.head.data)
        
        while current.next is not None:
            if current.next.data in hash:
                current.next = current.next.next
            else:
                hash.add(current.next.data)
                current = current.next
        return head
    
if __name__ == "__main__":
    list1 = LinkedList()
    list1.head = Node(10)
    second = Node(12)
    third = Node(11)
    fourth = Node(11)
    fifth = Node(12)
    sixth = Node(11)
    seventh = Node(10)
     
    list1.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    
    print("The given linked list:")
    list1.printList()
    list1.RemoveDuplicates(list1.head)
    print("\n After removing duplicates: ")
    list1.printList()
        