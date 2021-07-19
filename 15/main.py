# stack--link  pro

# 双链表

class node:
    def __init__(self, data):
        self.nextid = None
        self.lastid = None
        self.data = data


# 加快add和pop
# 构建双向链表


class link:

    def __init__(self):
        self.head = None
        self.size = 0
        self.last = None

    def add(self, data):
        point = node(data)
        if self.head is not None:
            point.lastid = self.last
            self.last.nextid = point
            self.last = point
        else:
            self.head = point
            self.last = point
        self.size += 1

    def pop(self):
        self.last = self.last.lastid
        self.last.nextid = None


class stack:

    def __init__(self):
        self.data = link()

    def push(self, x):
        self.data.add(x)

    def pop(self):
        x = self.data.last
        self.data.pop()
        return x.data

    def top(self):
        x = self.data.last
        return x.data

    def empty(self):
        if self.data.head is None:
            return False
        else:
            return True


sta = stack()

sta.push(1)
sta.push("helo")
sta.push([9377, True])

print(sta.empty())
print(sta.pop())
print(sta.top())
