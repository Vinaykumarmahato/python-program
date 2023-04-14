from dataclasses import dataclass


class node:
    def __init__(self,data):
        self.data=data
        self.node=None
        class singlelinkedlist:
            def __init__(self):
                self.head=None
                def display(self):
                    if self.head is None
                    print("linked list is empitty")
                else:
                    temp=self.head
                    while temp:
                        print(temp.data,"-->",end="")
                        temp=temp.next
l=singlelinkedlist()
n=node(10)
l.head=n
n1=node(20)
l.head.next=n1
n2=node(30)
n1.next=n2
l.displayaaa()