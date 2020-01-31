# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        stack = [(t1,t2)]
        while(stack):
            node = stack.pop(0)
            node[0].val += node[1].val

            if node[0].left and node[1].left:
                stack.append((node[0].left, node[1].left))
            elif node[1].left:
                node[0].left = node[1].left

            if node[0].right and node[1].right:
                stack.append((node[0].right, node[1].right))
            elif node[1].right:
                node[0].right = node[1].right

        return t1

