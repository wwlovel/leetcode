# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        queue = []
        queue.append(root)
        while(queue):
            curr = queue.pop(0)
            tmp = curr.left
            curr.left = curr.right
            curr.right = tmp
            if (curr.right): queue.append(curr.right)
            if (curr.left): queue.append(curr.left)
        return root
    def invertTree(self, root):
        if root is None:
            return root
        root.left, root.right = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root