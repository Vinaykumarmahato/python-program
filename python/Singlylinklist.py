# A single node of a singly linked list

class node:
    # constructor
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next
        # A linked list class with a single heade node
        class linkedlist:
            def __init__(self):
                self.head = None
                # Insertion method for the linked l
                def insert(self, data):
                    newNode = Node(data)
                    if(self.head):
                        current = self.head
                        current.next = newNode
                    else:
                        self.head = newNode
                        # Print method for linked list
                        def printLL(self):
                            current = self.head
                            while(current):
                                print(current.data)
                                current = current.next
                                # Singly linked list with insertion and print methods
                                LL  = linkedlist()
                                LL.insert(3)
                                LL.insert(4)
                                LL.insert(5)
                                LL.printLL()