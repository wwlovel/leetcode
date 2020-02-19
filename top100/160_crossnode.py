# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p = headA
        q = headB
        while (p != q):
            p = p.next if p else headB
            q = q.next if q else headA
        return p

t = ListNode(1)
headA = t
for i in [2,5,7,9,11]:
    t.next = ListNode(i)
    t = t.next
while(headA):
    print(headA.val)
    headA = headA.next

t = ListNode(2)
headB = t
for i in [4,9,11]:
    t.next = ListNode(i)
    t = t.next

s = Solution()
print(s.getIntersectionNode(headA, headB))