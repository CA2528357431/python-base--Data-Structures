# 二叉树

# 27非递归遍历

class tree:

    def __init__(self, root, left=None, right=None):
        self.nodes = []
        self.root = root
        self.left = left
        self.right = right

    @property
    def lisp(self):
        lisp = [self.root, None, None]
        if self.left is not None:
            lisp[1] = self.left.lisp
        if self.right is not None:
            lisp[2] = self.right.lisp
        return lisp
        # lisp 表达法

    def __str__(self):
        return str(self.lisp)

    def first(self):
        stack = []
        cur = self
        res = []
        while cur is not None or stack:
            # 遍历到左子树最下边的叶子节点，并保存遍历过程中的节点
            while cur is not None:
                stack.append(cur)
                res.append(cur.root)
                cur = cur.left
            # 开始出栈
            if stack:
                cur = stack.pop().right

        return res



    # 二叉树非递归中序遍历
    def middle(self):
        stack = []
        cur = self
        res = []
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            if stack:
                cur = stack.pop()
                res.append(cur.root)
                cur = cur.right

        return res

    # 二叉树非递归后序序遍历
    def last(self):
        stack = []
        cur = self
        res = []
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                if cur.left is not None:
                    cur = cur.left
                else:
                    cur = cur.right
            cur = stack.pop()
            res.append(cur.root)
            if stack and stack[len(stack)-1].left == cur:
                cur = stack[len(stack)-1].right
            else:
                cur = None
        return res

a = tree(1)
b = tree(2)
c = tree(3, a, b)
d = tree(6)
e = tree(4)
f = tree(10, d, e)
g = tree(13, c, f)

print(g.first())
print(g.middle())
print(g.last())
