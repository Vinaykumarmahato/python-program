class Node:

   def __init__(self,data,nextNode=None):
       self.data = data
       self.nextNode = nextNode

   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode


   def setNextNode(self,val):
       self.nextNode = val
       

class LinkedList:

   def __init__(self,head = None):
       self.head = head
       self.size = 0

   def getSize(self):
       return self.size

   def addNode(self,data):
       newNode = Node(data,self.head)
       self.head = newNode
       self.size+=1
       return True
       
   def printNode(self):
       curr = self.head
       while curr:
           print(curr.data)
           curr = curr.getNextNode()

myList = LinkedList()
print("Inserting")
print(myList.addNode(5)) 
print(myList.addNode(15))
print(myList.addNode(25))
print(myList.addNode(55))
print(myList.addNode(22))  
print(myList.addNode(12))
print(myList.addNode(23))
print(myList.addNode(140211021))
print(myList.addNode(15458))
print(myList.addNode(85))
print(myList.addNode(6265))
print(myList.addNode(124))
print(myList.addNode(14885))
print(myList.addNode(768554417))
print(myList.addNode(7569))
print(myList.addNode(655245))
print(myList.addNode(4782588))
print(myList.addNode(8528528))
print(myList.addNode(650))
print(myList.addNode(6545))
print(myList.addNode(6596))
print(myList.addNode(6554))
print(myList.addNode(6552645))


print("Printing")
myList.printNode()
print("Size")
print(myList.getSize())



