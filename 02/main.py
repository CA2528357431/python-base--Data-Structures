# 完整的链表

class linkpoint:
    def __init__(self, data, nextid=None):
        self.nextid = nextid
        self.data = data


class link:

    def __init__(self):
        self.head = None
        self._size = 0

    # for
    def __iter__(self):
        self.parser = 0
        self.current = self.head
        return self

    def __next__(self):

        if self.parser < self._size:
            now = self.current
            self.current = self.current.nextid
            self.parser += 1
            return now
        else:
            raise StopIteration

    def __len__(self):
        return self._size

    # 用get可以提高其他模块的编写
    def get(self, num):

        self.check(num)

        current = self.head
        parser = 0
        while parser < num:
            current = current.nextid
            parser += 1
        return current

    def add(self, data):

        node = linkpoint(data)
        if self.head is None:
            self.head = node
        else:
            current = self.get(self._size - 1)
            current.nextid = node
        self._size += 1

    def pop(self, num):

        if num == 0:
            self.head = self.head.nextid
        else:
            current = self.get(num - 1)
            current.nextid = current.nextid.nextid
        self._size -= 1

    def insert(self, data, num):

        node = linkpoint(data)
        if num == 0:
            node.nextid = self.head
            self.head = node
        else:
            current = self.get(num - 1)
            node.nextid = current.nextid
            current.nextid = node

        self._size += 1

    def index(self, data):
        parser = 0
        for x in self:
            if x.data == data:
                return parser
            parser += 1
        return -1

    def indexall(self, data):
        parser = 0
        li = []
        for x in self:
            if x.data == data:
                li.append(parser)
            parser += 1
        return li


    def remove(self, data):
        parser = self.index(data)
        self.pop(parser)

    def removeall(self, data):
        li = self.indexall(data)
        for x in li:
            self.pop(x)

    def check(self, num):
        if num >= self._size or num < 0:
            raise IndexError



    def reverse(self):
        last = None

        for x in range(0,self._size):
            current = self.head
            self.head = current.nextid
            current.nextid = last
            last = current
        self.head = last


    def sort(self):
        for _ in range(0,self._size):
            for x in self:
                if x.nextid is not None:
                    if x.data>x.nextid.data:
                        temp = x.data
                        x.data = x.nextid.data
                        x.nextid.data = temp




'''----------------TEST------------------'''


ex = link()
ex.add("hello")
ex.add("how are you")
ex.add("i am fine")
ex.add("that's good")
ex.add("see you")
ex.add("bye")

'''

for x in ex:
    print(id(x))



print(len(ex))



for x in ex:
    print(x.data)
print(ex.get(2).data)



ex.pop(5)
for x in ex:
    print(x.data)



ex.insert("get away", 2)
for x in ex:
    print(x.data)



i = ex.index("hello")
print(i)
ii = ex.get(i)
print(ii.data)



ex.remove("hello")
for x in ex:
    print(x.data)



ex.add("bye")
for x in ex:
    print(x.data)
print(ex.indexall("bye"))
ex.removeall("bye")
for x in ex:
    print(x.data)



ex.reverse()
for x in ex:
    print(x.data)



ex.sort()
for x in ex:
    print(x.data)
    
'''

