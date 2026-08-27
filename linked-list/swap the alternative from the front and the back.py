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
node7=Node(70)
node8=Node(80)
node9=Node(90)
node10=Node(100)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7
node7.next=node8
node8.next=node9


head=node1
fast=head
slow=head
while fast.next and fast.next.next:
    slow=slow.next
    fast=fast.next.next

headB=slow.next
slow.next=None
slow=headB
prev=None

curr=headB
while curr:
    nxt=curr.next
    curr.next=prev
    prev=curr
    curr=nxt
headB=prev
current=head
current2=headB




while current and current2:
    cu_nxt=current.next
    cu2_nxt=current2.next
    current.next=current2
    current2.next=cu_nxt
    current=cu_nxt
    current2=cu2_nxt

current=head
while current :
    print(current.data)
    current=current.next