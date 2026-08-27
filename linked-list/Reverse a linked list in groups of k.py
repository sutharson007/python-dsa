class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def reversed_list(k,head):
    current=head
    prev_group_tail=None
    new_head=None

    while current is not None:
        group_end=current
        count=1

        while count<k and  group_end is not None:
            count+=1
            group_end=group_end.next
        if group_end is None:
            break
        next_group=group_end.next
        prev=next_group
        node=current
        while node!=next_group:
            next_node=node.next
            node.next=prev
            prev=node
            node=next_node
        if new_head is None:
            new_head=group_end
        if prev_group_tail is not None:
            prev_group_tail.next=group_end
        prev_group_tail=current
        current=next_group
    if new_head is None:
        return head
    return new_head



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
head = node1

k = 2
head = reversed_list(k,head)
current = head

while current is not None:
    print(current.data)
    current = current.next


    