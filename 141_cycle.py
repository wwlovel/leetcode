# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle2(self, head: ListNode) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        p = head
        q = head.next
        while(p != q):
            if p is None or q is None:
                return False
            p = p.next
            q = q.next.next
        return True
