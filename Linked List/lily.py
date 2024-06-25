class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
dummy = Node(0)
cur = dummy


for i in range(1,6):
    cur.next = Node(i)
    cur = cur.next
    
cur = dummy.next
    
while cur:
    print(cur, cur.val)
    cur = cur.next
    
a = Node(1)
b = Node(2)

a.next = b


