# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first_start = head
        first_end = self.get_first_end(head)
        second_start = self.reverse_link(first_end.next)
        while(second_start):
            if first_start.val != second_start.val:
                return False
            first_start = first_start.next
            second_start = second_start.next
        return True



    def get_first_end(self, head):
        slow = head
        fast = head
        while(fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_link(self, node):
        prev = None
        curr = node
        while(curr):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

