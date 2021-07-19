# 循环单链表

class node:
    def __init__(self, data, nextid=None):
        self.nextid = nextid
        self.data = data


class link:
    def __init__(self):
        self.head = None
        self.size = 0
        self.last = None

    def add(self, data):
        point = node(data)
        if self.head is None:
            self.head = point
            self.last = point
        else:
            self.last.nextid = point
            self.last = point
        self.size += 1
        self.last.nextid = self.head

    def pop(self):
        self.head = self.head.nextid
        self.size -= 1
        self.last.nextid = self.head



    def get(self, x):
        par = 0
        cur = self.head
        while par < x:
            par += 1
            cur = cur.nextid
        return cur


beta = link()
for x in range(0,10):
    beta.add(x)
cur = beta.get(beta.size - 1)
print(cur.data)
next = cur.nextid
print(next.data)
