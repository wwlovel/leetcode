# Definition for a binary tree node.
#https://blog.csdn.net/Bone_ACE/article/details/46718683
class TreeNode(object):
    def __init__(self, x=-1):
        self.val = x
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = TreeNode()
        self.myQueue = []
    def add(self, elem):
        node = TreeNode(elem)
        if self.root.val == -1:
            #空树
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(node)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                #右孩子也有值，则该结点满了，下一个结点
                self.myQueue.pop(0)

    def bfs(self, root):
        if root == None:
            return root
        queue = [root]
        return_list = []
        while(queue):
            node = queue.pop(0)
            return_list.append(node.val)
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)
        return return_list

    def digui_front(self, root):
        if root is None:
            return
        print(root.val,end=",")
        self.digui_front(root.lchild)
        self.digui_front(root.rchild)

    def stack_front(self, root):
        if root is None:
            return root
        stack = []
        a = root
        while(a or stack):
            while(a):
                print(a.val,end=",")
                stack.append(a)
                a = a.lchild
            a = stack.pop()
            a = a.rchild

    def flag_front(self, root):
        if root is None:
            return root
        stack = [(root,0)]
        while(stack):
            node, flag = stack.pop()
            if node == None:
                continue
            if flag == 0:
                stack.append((node.rchild, 0))
                stack.append((node.lchild, 0))
                stack.append((node,1))
            else:
                print(node.val,end=",")

    def digui_mid(self, root):
        if root == None:
            return
        self.digui_mid(root.lchild)
        print(root.val,end=",")
        self.digui_mid(root.rchild)

    def stack_mid(self, root):
        if root == None:
            return root
        stack = []
        a = root
        while(a or stack):
            while(a):
                stack.append(a)
                a = a.lchild
            a = stack.pop()
            print(a.val,end=",")
            a = a.rchild

    def flag_mid(self, root):
        if root == None:
            return root
        stack = [(root, 0)]
        while(stack):
            node, flag = stack.pop()
            if node == None:
                continue
            if flag == 0:
                stack.append((node.rchild,0))
                stack.append((node,1))
                stack.append((node.lchild,0))
            else:
                print(node.val, end=",")

    def digui_later(self, root):
        if root == None:
            return
        self.digui_later(root.lchild)
        self.digui_later(root.rchild)
        print(root.val, end=",")

    def stack_later(self, root):
        ###根右左逆序
        if root == None:
            return root
        stack1 = []
        ##根右左
        stack2 = []
        a = root
        while(a or stack2):
            while(a):
                stack1.append(a.val)
                stack2.append(a)
                a = a.rchild
            a = stack2.pop()
            a = a.lchild
        while stack1:
            a = stack1.pop()
            print(a, end=",")

    def flag_later(self, root):
        if root == None:
            return root
        stack = [(root, 0)]
        while(stack):
            node, flag = stack.pop()
            if node == None:
                continue
            if flag == 0:
                stack.append((node, 1))
                stack.append((node.rchild,0))
                stack.append((node.lchild,0))
            else:
                print(node.val, end=",")




if __name__=='__main__':
    tree = Tree()
    elems = [0,1,2,3,4,5,6,7,8,None,None,None,None,None,10]
    for i in elems:
        tree.add(i)
    print("层次遍历:")
    print(tree.bfs(tree.root))
    print("先序：根左右")
    print(tree.digui_front(tree.root))
    print(tree.stack_front(tree.root))
    print(tree.flag_front(tree.root))

    print("中序：左根右")
    print(tree.digui_mid(tree.root))
    print(tree.stack_mid(tree.root))
    print(tree.flag_mid(tree.root))

    print("后序：左右根")
    print(tree.digui_later(tree.root))
    print(tree.stack_later(tree.root))
    print(tree.flag_later(tree.root))

