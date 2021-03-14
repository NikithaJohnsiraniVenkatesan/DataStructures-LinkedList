#How do you find the sum of two linked lists using Stack?
#We are going to add two linked list and output the sum

#traverse both the linked list from start to end
#add two digits each from representative linked list
#if one of the list has reached its end take 0 as digit for the remaining space

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
        
    def AddTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0
        
        while(first is not None or second is not None):
            firstdata = 0 if first is None else first.data
            seconddata = 0 if second is None else second.data
            summation = carry + firstdata + seconddata
            
            carry = 1 if summation > 10 else 0
            summation = summation if summation < 10 else summation % 10
            
            temp = Node(summation)
            
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            
            prev = temp
            if first is not None:
                first = first.next
            if second is not None:
                second = second.next
        if carry > 0:
            temp.next = Node(carry)
    def PrintList(self):
        temp = self.head
        while(temp):
            out = temp.data
            temp = temp.next
            print(out, temp)
            
first = LinkedList()
second = LinkedList()
result = LinkedList()

first.push(1)
first.push(8)
print("The first Linked List is:", first.PrintList())

second.push(2)
print("The second Linked List is: ", second.PrintList())

result.AddTwoLists(first.head, second.head)
print("The summation of the two linked list is: ", result.PrintList())

            
            