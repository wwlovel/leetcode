# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        node = root
        zhan = []
        total = 0
        while zhan or node is not None:
            while node is not None:
                zhan.append(node)
                node = node.right
            node = zhan.pop(-1)
            total += node.val
            node.val = total
            node = node.left
        return root

