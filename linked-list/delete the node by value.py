class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

head=node1
current=head
target=30
while current.next is  not None:

    if current.next.data==30:
        current.next=current.next.next
    current=current.next