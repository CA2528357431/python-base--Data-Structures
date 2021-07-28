# dic--list

# 增改、删除、检索都是O（n），慢

class data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        re = str(self.key) + ": " + str(self.value)
        return re


class mydic:
    def __init__(self):
        self.alldata = []

    def __str__(self):
        re = [str(x) for x in self.alldata]
        res = "{\n" + ",\n".join(re) + "\n}"
        return res

    @property
    def size(self):
        return len(self.alldata)

    @property
    def keys(self):
        keys = [x.key for x in self.alldata]
        return keys

    def addchange(self, key, value):
        if key not in self.keys:
            neo = data(key, value)
            self.alldata.append(neo)
        else:
            for x in self.alldata:
                if x.key == key:
                    x.value = value
                    break

    def pop(self, key):
        if key in self.keys:
            for i in range(0, self.size):
                if self.alldata[i].key == key:
                    self.alldata.pop(i)

    def seek(self, key):
        for x in self.alldata:
            if x.key == key:
                return x.value
        return None


dic = mydic()

dic.addchange("neo", 2)
dic.addchange("old", [True, False])
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
