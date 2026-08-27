from ftplib import parse150


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)

node1.next=node3
node3.next=node4
node2.next=node4
node4.next=node5


p1=node1
p2=node2
Found=False
while p1 is not None and p2 is not None:
    if p1 == node2:
        print("Intersection")
        Found=True
        break
    p1=p1.next
    p2=p2.next
if not Found:
    print("Not intersection")

