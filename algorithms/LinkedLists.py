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

        print(current.data)
        print(current.next)
        print(current.data)
        


ll = linkedList()

ll.addFirst(400)
ll.addFirst(300)
ll.addFirst(200)
ll.addFirst(100)

ll.displayAll()
