# stack-link

# first in last out

class node:
    def __init__(self, data):
        self.nextid = None
        self.data = data


class link:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, x):
        parser = 0
        current = self.head
        while parser < x:
            parser += 1
            current = current.nextid
        return current

    def add(self, data):
        point = node(data)
        if self.head is not None:
            current = self.get(self.size - 1)
            current.nextid = point
        else:
            self.head = point
        self.size += 1

    def pop(self):
        current = self.get(self.size - 2)
        current.nextid = None
        self.size -= 1


class stack:
    def __init__(self):
        self.data = link()

    def push(self, x):
        self.data.add(x)

    def pop(self):
        x = self.data.get(self.data.size - 1)
        self.data.pop()
        return x.data

    def top(self):
        x = self.data.get(self.data.size - 1)
        return x.data

    def empty(self):
        if self.data.head is None:
            return False
        else:
            return True

sta = stack()

sta.push(1)
sta.push("helo")
sta.push([9377,True])

print(sta.empty())
print(sta.pop())
print(sta.top())