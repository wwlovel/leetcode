# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal_diedai(self, root):
        """
        迭代法中序遍历，左，跟，右
        先该点的左孩子全部入栈，
        没有左孩子，弹栈，再判断右孩子
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        node = root
        stack = []
        a = []
        while(stack or node is not None):
            while(node):
                stack.append(node)
                node = node.left
            node = stack.pop()
            a.append(node.val)
            node = node.right
        return a
    def inorderTraversal_yanse(self, root):
        """
        未访问白色，已访问灰色
        :type root: TreeNode
        :rtype: List[int]
        """
        w, g = 1, 0
        stack = [(w, root)]
        a = []
        while(stack):
            color, node = stack.pop()
            if node is None:
                continue
            if color == w:
                stack.append((w,node.right))
                stack.append((g, node))
                stack.append((w, node.left))
            else:
                a.append(node.val)
        return a

    def preorderTraversal_yanse(self, node):
        w, g = 1, 0
        a = []
        stack = [(w, node)]
        while(stack):
            color, node = stack.pop()
            if node is None:
                continue
            if color == w:
                stack.append((w, node.right))
                stack.append((w, node.left))
                stack.append((g, node))
            else:
                a.append(node.val)
        return a
    def postorderTraversal_yanse(self, node):
        w, g = 1, 0
        a = []
        stack = [(w, node)]
        while(stack):
            color, node = stack.pop()
            if node is None:
                continue
            if color == w:
                stack.append((g, node))
                stack.append((w, node.right))
                stack.append((w, node.left))
            else:
                a.append(node.val)
        return a