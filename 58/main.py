# 最佳二叉排序树

# 类似哈夫曼树，不过哈夫曼树中数据都在叶节点中，而最佳二叉树各个节点都有数据

# 在通常情况下，使树尽可能平衡即可

class node:
    def __init__(self, key, left=None, right=None, data=None):
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
            re.append("\n")
            neoqueue = []
            for item in queue:
                if item:
                    neoqueue.append(item.left)
                    neoqueue.append(item.right)
            queue = neoqueue
        res = []
        for i in range(0, len(re)):
            if re[i] is None:
                res.append("None ")
            elif re[i] == "\n":
                res.append("\n")
            else:
                res.append(str(re[i].key).ljust((5)))
        string = "".join(res)
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


def perfecttree(keys: list):
    mid = len(keys) // 2
    lkeys = keys[:mid]
    rkeys = keys[mid+1:]
    root = node(keys[mid])
    tre = bintree(root)
    if lkeys:
        tre.root.left = perfecttree(lkeys).root
    if rkeys:
        tre.root.right = perfecttree(rkeys).root
    return tre

keys = [1,5,3,9,11,0,23,8]
keys.sort()
print(perfecttree(keys))

print()
print()

tre = bintree()
keys = [1,5,3,9,11,0,23,8]
for x in keys:
    tre.add(node(x))
print(tre)