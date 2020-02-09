import time as t

import
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    

class linkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addFirst(self,data):
            self.head = Node(data, self.head)
            self.size += 1
    
    def displayAll(self):
        current = self.head

        while(current):
            print(current.data)
            current = current.next
    
    def displayOne(self,index):
        current = self.head

        if current.size < index:
            print("out of scope")
        while(current.next != None):
            if current.data == index:
                print(current.data)
            current = current.next 

    def addLast(self,data):
        node = Node(data)
        current = None

        if self.head == None:
            self.head = node 
        else:
            current = self.head

            while(current.next != None):
                current = current.next
            current.next = node
        
        self.size += 1
    
    def insertAt(self,index,data):
        node = Node(data)

        



start_time = t.time()

ll = linkedList()

ll.addFirst(400)
ll.addFirst(300)
ll.addFirst(200)
ll.addFirst(100)
ll.addLast(1000)

print(ll.size)


ll.displayAll()

end_time = t.time()


print(f"The program ran for {end_time - start_time} seconds")
