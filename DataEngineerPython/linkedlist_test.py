class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#就地反转
def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev


# 递归反转
def recursiveReverse(head):
    if head is None or head.next is None:
        return head
    
    p = head.next
    newHead = recursiveReverse(p)
    p.next = head
    head.next = None
    
    return newHead


#插入反转
def insertReverse(head):
    if head is None or head.next is None:
        return
    
    cur = head.next
    head.next = None
    
    while cur is not None:
        next = cur.next
        
        cur.next = head
        head = cur
        cur = next
    

def newLNode():
    # 示例用法
    # 创建一个链表：1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    return head

# 反转链表
head = newLNode()
reversed_head = reverseList(head)

# 输出反转后的链表
while reversed_head:
    print(reversed_head.val, end=" ")
    reversed_head = reversed_head.next
print()

head2 = newLNode()
new_r_head = recursiveReverse(head2)
while new_r_head:
    print(new_r_head.val, end=" ")
    new_r_head = new_r_head.next
print()

head3 = newLNode()
rh = insertReverse(head3)
while head3:
    print(head3.val, end=" ")
    head3 = head3.next
print()


