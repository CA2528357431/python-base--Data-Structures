# queue-link   pro

class node:
    def __init__(self, data):
        self.data = data
        self.nextid = None


class link:
    def __init__(self):
        self.head = None
        self.size = 0
        self.last = None
        # 加快add获取最后node操作

    def add(self, data):
        point = node(data)
        if self.head is None:
            self.head = point
            self.last = point
        else:
            self.last.nextid = point
            self.last = point
        self.size += 1

    def pop(self):
        self.head = self.head.nextid
        self.size -= 1


class queue:
    def __init__(self):
        self.link = link()

    def add(self, data):
        self.link.add(data)

    def pop(self):
        cur = self.link.head
        self.link.pop()
        return cur

    def top(self):
        cur = self.link.head
        return cur

    def empty(self):
        if self.link.head:
            return False
        else:
            return True


hk = queue()
for x in range(0,10):
    hk.add(x)
    y = hk.top()
    print(y.data)
for _ in range(0,10):
    y = hk.pop()
    print(y.data)
print(hk.empty())