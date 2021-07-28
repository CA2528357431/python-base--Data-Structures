# 集合


class aggregate:
    def __init__(self):
        self.data = []

    def __str__(self):
        re = [str(x) for x in self.data]
        res = "{" + ", ".join(re) + "}"
        return res

    def __contains__(self, item):
        return item in self.data

    @classmethod
    def union(cls, a, b):
        res = aggregate()
        res.data = a.data.copy()
        for x in b.data:
            if x not in a.data:
                res.data.append(x)
        return res

    @classmethod
    def intersection(cls, a, b):
        res = aggregate()
        for x in a.data:
            if x in b.data:
                res.data.append(x)
        return res

    @classmethod
    def minus(cls, a, b):
        res = aggregate()
        for x in a.data:
            if x not in b.data:
                res.data.append(x)
        return res

    def add(self, x):
        self.data.append(x)

    def pop(self, x):
        self.data.remove(x)




a = aggregate()
a.data = [1, 2]
b = aggregate()
b.data = [1, 3]
c = aggregate.union(a, b)
d = aggregate.intersection(a, b)
e = aggregate.minus(a, b)
print(c)
print(d)
print(e)
print()

e.add(9377)
print(e)
print()

e.pop(2)
print(e)
print()

print(9377 in e)
