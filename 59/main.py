# AVL树

# 我们如果要在增删之后保持树的完美，必然会付出大量成本
# 因此我们不妨选择更 宽松 的结构

# 平衡二叉树，每个节点的子树相差高度最多为1
# 整体上看可能很 偏
# 图中展示的是 最偏 的平衡树


# 插入一个节点后，只有从插入节点到根节点的路径上的节点的平衡可能被改变。
# 我们需要找出第一个破坏了平衡条件的节点，称之为K。K的两颗子树的高度差2。
# 不平衡有四种情况：
# 1.对K的左儿子的左子树进行一次插入
# 2.对K的左儿子的右子树进行一次插入
# 3.对K的右儿子的左子树进行一次插入
# 4.对K的右儿子的右子树进行一次插入
# 14对称，23对称


class node:
    def __init__(self, key, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key
        # 就不设data了

    @property
    def height(self):
        l = 0
        r = 0
        if self.right:
            r = self.right.height
        if self.left:
            l = self.left.height
        return max(l, r) + 1

    @property
    def balance(self):
        l = 0
        r = 0
        if self.right:
            r = self.right.height
        if self.left:
            l = self.left.height
        return l - r
        # 左右子树之差


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
        self._recoveradd(neo.key)

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
            # 能找到key
            if last is None:
                # 删除根节点
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
        self._recoverdelete(key)

    def mid(self):
        l = []
        r = []
        if self.root.left:
            l = bintree(self.root.left).mid()
        if self.root.right:
            r = bintree(self.root.right).mid()
        return l + [(self.root.key, self.root.data)] + r

    # https://blog.csdn.net/weixin_45666566/article/details/108092977

    @classmethod
    def _llrecover(cls, knode):
        a = knode
        b = knode.left
        c = knode.left.right
        a.left = c
        b.right = a

        return b

    @classmethod
    def _rrrecover(cls, knode):
        a = knode
        b = knode.right
        c = knode.right.left
        a.right = c
        b.left = a
        return b

    @classmethod
    def _lrrecover(cls, knode):
        a = knode.left
        b = knode.left.right
        c = knode.left.right.left
        a.right = c
        b.left = a

        a = knode
        b = knode.left
        c = knode.left.right
        a.left = c
        b.right = a

        return b

    @classmethod
    def _rlrecover(cls, knode):
        a = knode.right
        b = knode.right.left
        c = knode.right.left.right
        a.left = c
        b.right = a

        a = knode
        b = knode.right
        c = knode.right.left
        a.right = c
        b.left = a

        return b

    def _recoveradd(self, key):
        fnode = None
        knode = None
        last = None
        cur = self.root
        while cur is not None and cur.key != key:
            if cur.balance > 1 or cur.balance < -1:
                fnode = last
                knode = cur
            last = cur
            if cur.key > key:
                cur = cur.left
            else:
                cur = cur.right

        if knode is not None:
            if knode.left is None:
                if knode.key <= key < knode.right.key:
                    knode = bintree._rlrecover(knode)
                else:
                    knode = bintree._rrrecover(knode)
            elif knode.right is None:
                if key < knode.left.key:
                    knode = bintree._llrecover(knode)
                else:
                    knode = bintree._lrrecover(knode)
            elif key<knode.left.key:
                knode = bintree._llrecover(knode)
            elif knode.left.key<=key<knode.key:
                knode = bintree._lrrecover(knode)
            elif knode.key<=key<knode.right.key:
                knode = bintree._rlrecover(knode)
            else:
                knode = bintree._rrrecover(knode)

            if fnode is None:
                self.root = knode
            elif key<fnode.key:
                fnode.left = knode
            else:
                fnode.right = knode


neo0 = node(13)
tre = bintree(neo0)
neo1 = node(3)
tre.add(neo1)
neo2 = node(16)
tre.add(neo2)
neo3 = node(6)
tre.add(neo3)
neo4 = node(10)
tre.add(neo4)
neo5 = node(11)
tre.add(neo5)
neo6 = node(0)
tre.add(neo6)
neo7 = node(1)
tre.add(neo7)
neo8 = node(7)
tre.add(neo8)
neo9 = node(17)
tre.add(neo9)
neo10 = node(1)
tre.add(neo10)
neo11 = node(8)
tre.add(neo11)
neo12 = node(17)
tre.add(neo12)

print(tre)

tre.delete(0)
print(tre)