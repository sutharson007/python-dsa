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
node2.next=node4
node3.next=node5
arr=[]
pointer1=node1
pointer2=node2
new_node=Node(None)
while pointer1 is not None or pointer2 is not None:
    if pointer1 is not None and pointer2 is not None:
        if pointer1.data<pointer2.data:
            arr.append(pointer1.data)
            pointer1=pointer1.next
        else:
            arr.append(pointer2)
            pointer2=pointer2.next
    elif pointer1 is not None:
        while pointer1 is not None:
            arr.append(pointer1.data)
    elif pointer2 is not None:
        while pointer2 is not None:
            arr.append(pointer2.data)
print(arr)

