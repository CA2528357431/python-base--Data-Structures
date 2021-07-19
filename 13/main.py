# queue--neo list

class queue:
    def __init__(self, size):
        self.size = size
        self.li = [None] * self.size
        self.head = None
        self.num = 0

    @property
    def last(self):
        index = self.head + self.num - 1
        if index > self.size - 1:
            return index - self.size
        else:
            return index

    def add(self, data):
        if self.head is None:
            self.li[0] = data
            self.head = 0
        elif self.num == self.size:
            self._extend()
            self.li[self.last + 1] = data
        else:
            self.li[self.last + 1] = data
        self.num += 1

    def _extend(self):
        # print("extend")
        li = [None] * (2 * self.size)
        for x in range(self.head, self.size):
            li[x] = self.li[x]
        for x in range(0, self.head):
            li[x] = self.li[x]
        self.li = li
        self.head = 0
        self.size = 2 * self.size

    def pop(self):
        cur = self.li[self.head]
        self.li[self.head] = None
        self.head += 1
        return cur

    def top(self):
        cur = self.li[self.head]
        return cur

    def empty(self):
        if self.li:
            return False
        else:
            return True


hk = queue(2)
for x in range(0,10):
    hk.add(x)
    y = hk.top()
    print(y)
for _ in range(0,10):
    y = hk.pop()
    print(y)
print(hk.empty())