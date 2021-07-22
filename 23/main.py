# 优先队列--list

class node:
    def __init__(self, data, prior):
        self.data = data
        self.prior = prior
        # 越大越优先


class priorqueue:

    def __init__(self):
        self.data = []

    def add(self, point):
        # self.data.append(point)
        # self.data.sort(lambda x: x.prior)
        # 以下为手写
        if not self.data:
            self.data.append(point)
        else:
            parser = len(self.data) - 1
            while parser >= 0 and self.data[parser].prior > point.prior:
                parser -= 1
            self.data.insert(parser + 1, point)

    def pop(self):
        x = self.data.pop()
        return x

    def top(self):
        x = self.data[len(self.data) - 1]
        return x

    def empty(self):
        if self.data:
            return False
        else:
            return True


a = node("hello", 2)
b = node(None, 1)
c = node([1, 2, 3], 9)
pri = priorqueue()
pri.add(a)
pri.add(b)
pri.add(c)
for _ in range(0, len(pri.data)):
    x = pri.pop()
    print(x.data)
print()
print(pri.empty())
