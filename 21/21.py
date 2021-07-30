# 二叉树

# 27非递归遍历


class tree:

    def __init__(self, root, left=None, right=None):
        self.nodes = []
        self.root = root
        self.left = left
        self.right = right

        self.data = None
        # root作为排序依据
        # data存数据

        # 后续几个二叉树用例就不带数据了

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

    # 三种深度优先遍历
    # 即三种周游
    # 周游一定是 根、左周游、右周游的组合

    def first(self):
        l = []
        r = []
        if self.left is not None:
            l = self.left.first()
        if self.right is not None:
            r = self.right.first()
        res = [self.root] + l + r

        return res

    '''
    def first(self):
        res = []
        cur = self
        def do(cur):
            if cur is not None:
                res.append(cur.root)
                do(cur.left)
                do(cur.right)
        do(cur)
        return res
    '''



    def middle(self):
        l = []
        r = []
        if self.left is not None:
            l = self.left.middle()
        if self.right is not None:
            r = self.right.middle()
        res = l + [self.root] + r

        return res

    '''
    def middle(self):
        res = []
        cur = self
        def do(cur):
            if cur is not None:
                do(cur.left)
                res.append(cur.root)
                do(cur.right)
        do(cur)
        return res
    '''

    def last(self):
        l = []
        r = []
        if self.left is not None:
            l = self.left.last()
        if self.right is not None:
            r = self.right.last()
        res =  l + r + [self.root]

        return res

    '''
    def last(self):
        res = []
        cur = self
        def do(cur):
            if cur is not None:
                do(cur.left)
                do(cur.right)
                res.append(cur.root)
        do(cur)
        return res
    '''

    # 一种广度优先遍历

    def layer(self):
        res = []
        queue = [self]
        # queue中同层的数据相连
        while queue:
            cur = queue[0]
            queue.pop(0)
            res.append(cur.root)
            for x in (cur.left,cur.right):
                if x is not None:
                    queue.append(x)
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
print(g.layer())
