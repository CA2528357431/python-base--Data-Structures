# queue-link

# first in first out

# add很慢，14有改进

class node:
    def __init__(self, data):
        self.data = data
        self.nextid = None


class link:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        parser = 0
        current = self.head
        while parser < index:
            parser += 1
            current = current.nextid
        return current

    def add(self,data):
        point = node(data)
        if self.head is None:
            self.head = point
        else:
            current = self.get(self.size-1)
            current.nextid = point
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
