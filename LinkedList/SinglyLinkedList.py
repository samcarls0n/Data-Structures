class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList():
        curr = self.head
        while curr:
            print(curr.data,end=‘’)
            curr = curr.next
        print()

    def insertAtFront(self, data):
        newest = Node(data)
        newest.next = self.head
        self.head = newest

     def insertAtEnd(self, data):
        newest = Node(data)
        if self.head is None:
            self.head = newest
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newest

     def deleteFromFront(self):
        if self.head is None:
            return
        self.head = self.head.next

     def deleteFromEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None
     
     def search(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                return True
            curr = curr.next
        return False

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtFront(1)
    ll.insertAtEnd(3)
    ll.insertAtEnd(5)
    ll.printList()
    ll.deleteFromFront()
    ll.deleteFromEnd()
    print(ll.search(3))