# 二叉排序树

# 若左子树不空，则左子树上所有结点的值均小于它的根结点的值
# 若右子树不空，则右子树上所有结点的值均大于或等于它的根结点的值
# 左、右子树也分别为二叉排序树

class node:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.data = data
# key决定在树里的位置
# data是数据

class bintree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        re = []
        queue = [self.root]
        while queue:
            re.extend(queue)
            neoqueue = []
            for item in queue:
                if item.left:
                    neoqueue.append(item.left)
                if item.right:
                    neoqueue.append(item.right)
            queue = neoqueue
        res = [str(x.key) for x in re]
        string = "\n".join(res)
        return string

    @property
    def empty(self):
        return self.root is None

    def search(self, key):
        cur = self.root
        while cur is not None and cur.key != key:
            if cur.key > key:
                cur = cur.left
            else:
                cur = cur.right
        if cur is not None:
            return cur.data
        else:
            return None

    def add(self, neo):
        cur = self.root
        if self.empty:
            self.root = neo
        else:
            while True:
                if neo.key < cur.key:
                    if cur.left is None:
                        cur.left = neo
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = neo
                        break
                    else:
                        cur = cur.right

    def delete(self, key):
        cur = self.root
        last = None
        while cur is not None and cur.key != key:
            last = cur
            if cur.key > key:
                cur = cur.left
            else:
                cur = cur.right

        if cur is not None:
            if last is None:
                par = cur.left
                parold = cur
                while par.right is not None:
                    parold = par
                    par = par.right
                parold.right = None
                self.root = par
                par.left = cur.left
                par.right = cur.right
            else:
                if cur.key < last.key:
                    if cur.left is None and cur.right is None:
                        last.left = None
                    elif cur.right is None:
                        last.left = cur.left
                    elif cur.left is None:
                        last.left = cur.right
                    else:
                        par = cur.left
                        parold = cur
                        while par.right is not None:
                            parold = par
                            par = par.right
                        parold.right = None
                        par.left = cur.left
                        par.right = cur.right
                        last.left = par
                # 树根是二子树的中值
                # 选择左树最右 或者右数最左


                else:
                    if cur.left is None and cur.right is None:
                        last.right = None
                    elif cur.right is None:
                        last.right = cur.left
                    elif cur.left is None:
                        last.right = cur.right
                    else:
                        par = cur.left
                        parold = cur
                        while par.right is not None:
                            parold = par
                            par = par.right
                        parold.right = None
                        par.left = cur.left
                        par.right = cur.right
                        last.right = par

    def mid(self):
        l = []
        r = []
        if self.root.left:
            l = bintree(self.root.left).mid()
        if self.root.right:
            r = bintree(self.root.right).mid()
        return l + [(self.root.key, self.root.data)] + r


neo0 = node(13, "hello")
tre = bintree(neo0)
neo1 = node(3, "evening")
tre.add(neo1)
neo2 = node(16, True)
tre.add(neo2)
neo3 = node(6, 97.41)
tre.add(neo3)
neo4 = node(10, [1, 5, False])
tre.add(neo4)

print(tre)
print()

print(tre.mid())
print()

x = tre.search(6)
print(x)
y = tre.search(7)
print(y)
print()

tre.delete(13)
print(tre)
