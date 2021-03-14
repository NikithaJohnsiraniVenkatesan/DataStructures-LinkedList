#How do you find the length of a singly linked list? 

#Initialize the count as 0 and node pointer and current = head
#While current is not null, current -> next and count++
#return the count value

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next =self.head
        self.head = new_node
    def GetCount(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count

if __name__ == '__main__':
    list1 = LinkedList()
    list1.push(2)
    list1.push(7)
    list1.push(98)
    list1.push(7)
    list1.push(12)
    
    print("The count of nodes is: ",list1.GetCount())