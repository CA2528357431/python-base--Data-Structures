def hash(key):
    sum = 139
    for x in key:
        sum += ord(x) * 19
    index = sum % 10

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
        self.alldata = []
        for _ in range(0,10):
            self.alldata.append([])
            # 或许链表也行？
    def __str__(self):
        lis = [x for x in self.alldata]
        re = []
        for li in lis:
            for x in li:
                re.append(str(x))
        res = "{\n" + ",\n".join(re) + "\n}"
        return res

    def __contains__(self, key):
        index = hash(key)
        for x in self.alldata[index]:
            if x.key == key:
                return True
        return False

    @property
    def size(self):
        sum = 0
        for li in self.alldata:
            sum += len(li)
        return sum

    @property
    def keys(self):
        lis = [x for x in self.alldata]
        keys = []
        for li in lis:
            for x in li:
                keys.append(x.key)
        return keys

    def add(self, key, value):
        if key not in self.keys:
            index = hash(key)
            neo = data(key, value)
            self.alldata[index].append(neo)

    def change(self, key, value):
        index = hash(key)
        for x in self.alldata[index]:
            if x.key == key:
                x.value = value

    def pop(self, key):
        if key in self.keys:
            index = hash(key)
            for x in range(0,len(self.alldata[index])):
                if self.alldata[index][x].key == key:
                    self.alldata[index].pop(x)

    def seek(self, key):
        index = hash(key)
        for x in self.alldata[index]:
            if x.key == key:
                return x

# b/v 索引一致，若无溢出处理，则会互相覆盖
print(hash("b"))
print(hash("v"))
print(hash("a"))
print(hash("c"))
print()

dic = mydic()

dic.add("a", 2)
dic.add("b", [True, False])
dic.add("c", "heool")
dic.add("d", 1111)
print(dic)
print()

dic.change("b", [1111,0])
print(dic)
print()

dic.pop("b")
print(dic)
print()

print(dic.keys)

print("a" in dic)


