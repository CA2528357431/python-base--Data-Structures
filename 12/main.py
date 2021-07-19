# queue--list base

class queue:
    def __init__(self):
        self.li = []

    def add(self, data):
        self.li.append(data)

    def pop(self):
        cur = self.li[0]
        self.li.pop(0)
        return cur

    def top(self):
        cur = self.li[0]
        return cur

    def empty(self):
        if self.li:
            return False
        else:
            return True


hk = queue()
for x in range(0,10):
    hk.add(x)
    y = hk.top()
    print(y)
for _ in range(0,10):
    y = hk.pop()
    print(y)
print(hk.empty())