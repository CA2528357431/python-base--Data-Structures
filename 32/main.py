# 树的遍历

class tree:

    def __init__(self, root):
        self.root = root
        self.child = []

    @property
    def numchild(self):
        return len(self.child)

    @property
    def degree(self):
        res = []
        queue = [self]
        while queue:
            cur = queue[0]
            queue.pop(0)
            res.append(cur.numchild)
            for x in cur.child:
                queue.append(x)
        return max(res)

    @property
    def height(self):
        i = 0
        queue = [self]
        while queue:
            i += 1
            neo = []
            for y in queue:
                for x in y.child:
                    neo.append(x)
            queue = neo
        return i

    def layer(self):
        res = []
        queue = [self]
        while queue:
            cur: tree = queue[0]
            queue.pop(0)
            res.append(cur.root)
            for x in cur.child:
                queue.append(x)
        return res

    def first(self):
        res = [self.root]
        for x in self.child:
            res.extend(x.first())
        return res

    def last(self):
        res = []
        for x in self.child:
            res.extend(x.last())
        res.append(self.root)
        return res


a = tree("a")

b = tree("b")
c = tree("c")
d = tree("d")
a.child.append(b)
a.child.append(c)
a.child.append(d)

e = tree("e")
f = tree("f")
g = tree("g")
h = tree("h")
i = tree("i")
b.child.append(e)
b.child.append(f)
c.child.append(g)
d.child.append(h)
d.child.append(i)

j = tree("j")
k = tree("k")
l = tree("l")
m = tree("m")
n = tree("n")
g.child.append(j)
g.child.append(k)
h.child.append(l)
i.child.append(m)
i.child.append(n)

res1 = a.layer()
print(res1)
print()

res2 = a.first()
print(res2)
print()

res3 = a.last()
print(res3)
print()

degree = a.degree
print(degree)
print()

height = a.height
print(height)
print()
