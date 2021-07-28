# dic--散列表

# 通过编写散列函数，将key映射到index上，从而实现快速修改
# 需要提前开一个list充满none作为物理容器，使得增加、删除快速



"""
hash编写
越混乱无序，越均匀越好
"""

def hash(key):
    sum = 139
    for x in key:
        sum += ord(x) * 19
    index = sum % 100

    return index

class data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        re = str(self.key)+": "+str(self.value)
        return re

class mydic:
    def __init__(self):
        self.alldata = [None]*100

    def __str__(self):
        re = [str(x) for x in self.alldata if x is not None]
        res = "{\n" + ",\n".join(re) + "\n}"
        return res

    @property
    def size(self):
        return len(self.alldata)

    @property
    def keys(self):
        keys = [x.key for x in self.alldata if x is not None]
        return keys

    def addchange(self, key, value):
        index = hash(key)
        neo = data(key, value)
        self.alldata[index] = neo

    def pop(self, key):
        index = hash(key)
        self.alldata[index] = None

    def seek(self, key):
        index = hash(key)
        return self.alldata[index]




dic = mydic()

dic.addchange("neo", 2)
dic.addchange("old", [True, False])
dic.addchange("well", "heool")
print(dic)
print()

dic.addchange("old", [])
print(dic)
print()

dic.pop("old")
print(dic)
print()

re1 = dic.seek("old")
re2 = dic.seek("neo")
print(re1, re2)