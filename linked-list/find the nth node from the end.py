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
slow=head
fast=node1
i=0
n=2
while fast.next is not None:

    fast=fast.next
    i+=1
    if i<=n+1:
        slow=slow.next
print(slow.data)