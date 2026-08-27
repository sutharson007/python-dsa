class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node1.next=node2
node2.next=node3
node3.next=node4
head=node1
position=1
current=head
for i in range(position-1):
    current=current.next
new_node=Node(15)
new_node.next=current.next
current.next=new_node