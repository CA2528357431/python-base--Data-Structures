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
        l = []
        r = []
        if self.left is not None:
            l = self.left.first()
        if self.right is not None:
            r = self.right.first()
        res = [self.root] + l + r

        return res



    def middle(self):
        l = []
        r = []
        if self.left is not None:
            l = self.left.middle()
        if self.right is not None:
            r = self.right.middle()
        res = l + [self.root] + r

        return res

    def last(self):
        l = []
        r = []
        if self.left is not None:
            l = self.left.last()
        if self.right is not None:
            r = self.right.last()
        res =  l + r + [self.root]

        return res

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


class stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.empty():
            return None
        else:
            x = self.data[len(self.data) - 1]
            self.data.pop()
            return x

    def top(self):
        if self.empty():
            return None
        else:
            return self.data[len(self.data) - 1]

    def empty(self):
        if self.data:
            return False
        else:
            return True


def swap(tar):
    sta = stack()
    data = tar.split(" ")
    res = []
    for x in data:
        if x in "()" :
            if x == "(":
                sta.push(x)
            else:
                while sta.top() != "(":

                    l = len(res)
                    t1 = res[l - 1]
                    t2 = res[l - 2]
                    res.pop()
                    res.pop()

                    t3 = tree(sta.top(), t2, t1)
                    res.append(t3)

                    sta.pop()

                sta.pop()
        elif x in "+-":
            if sta.empty():
                sta.push(x)
            elif sta.top() in "*/":
                cur = sta.pop()

                l = len(res)
                t1 = res[l - 1]
                t2 = res[l - 2]
                res.pop()
                res.pop()

                t3 = tree(cur, t2, t1)
                res.append(t3)

                sta.push(x)
            else:
                sta.push(x)
        elif x in "*/":
            sta.push(x)
        else:
            t = tree(x)
            res.append(t)

    while not sta.empty():
        cur = sta.pop()

        l = len(res)
        t1 = res[l - 1]
        t2 = res[l - 2]
        res.pop()
        res.pop()

        t3 = tree(cur, t2, t1)
        res.append(t3)

    return res[0]


tar = "( a + ( b + c ) * d ) - e"
res = swap(tar)
print(res)