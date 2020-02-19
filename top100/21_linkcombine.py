# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1
        q = l2
        if p.val >= q.val:
        	r = q
        	q = q.next
        else:
        	r = p
        	p = p.next
        ret = r
        while p is not None or q is not None:
        	if p.val > q.val:
        		r = q
        		q = q.next
        	else:
        		r = p
        		p = p.next
        	r = r.next
        return ret

