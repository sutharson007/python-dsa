class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

## for the deletion from the start

head=node2
node1.next=None

## for the deletion at the end

current=head
while current.next.next is not None:
    current=current.next
current.next=None
print(current.data)
print(current.next)

## delete the node at the beginning
current=head
position=2

while current.next is not None:
    if current.next.data == 20:
        current.next = current.next.next
        break
    current = current.next