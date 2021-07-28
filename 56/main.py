# 集合

def hash(key):
    sum = 1097

    # 由于不知道数据类型，所以把type加入hash
    for x in str(key) + str(type(key)):
        sum += ord(x) * 593
    index = sum % 1000

    return index


class aggregate:
    def __init__(self):
        self.data = [None]*1000

    def __str__(self):
        re = [str(x) for x in self.data if x is not None]
        res = "{" + ", ".join(re) + "}"
        return res

    def __contains__(self, value):
        index = hash(value)
        return self.data[index] is not None

    @property
    def size(self):
        res = 0
        for x in self.data:
            if x is not None:
                res += 1
        return res

    def add(self, value):
        index = hash(value)
        self.data[index] = value

    def pop(self, value):
        index = hash(value)
        self.data.pop(index)

    @classmethod
    def union(cls, a, b):
        neo = aggregate()
        for x in range(0, 1000):
            if a.data[x] is not None:
                neo.data[x] = a.data[x]
            elif b.data[x] is not None:
                neo.data[x] = b.data[x]
        return neo

    @classmethod
    def intersection(cls, a, b):
        neo = aggregate()
        for x in range(0, 1000):
            if (a.data[x] is not None) and (b.data[x] is not None):
                neo.data[x] = a.data[x]
        return neo

    @classmethod
    def minus(cls, a, b):
        neo = aggregate()
        for x in range(0, 1000):
            if (a.data[x] is not None) and (b.data[x] is None):
                neo.data[x] = a.data[x]
        return neo

a = aggregate()
a.add(1)
a.add("1")
a.add(2)
b = aggregate()
b.add(1)
b.add(3)
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

