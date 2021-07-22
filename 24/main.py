# prior--堆heap

class node:
    def __init__(self, data, prior):
        self.data = data
        self.prior = prior
        # 越大越优先 大于0


class heap:

    def __init__(self):
        self.data = []

    def __str__(self):
        res = []
        for x in self.data:
            res.append(x.data)
        return str(res)

    def empty(self):
        if self.data:
            return False
        else:
            return True

    def add(self, point):
        self.data.append(point)
        j = len(self.data) - 1
        i = (j - 1) // 2
        so = self.data[j]
        fa = self.data[i]
        while i >= 0 and fa.prior < so.prior:
            self.data[i] = so
            self.data[j] = fa
            j = i
            i = (j - 1) // 2
            so = self.data[j]
            fa = self.data[i]

    # 把新元素加到末尾
    # 只要新元素优先级高于父元素，就交换父子位置


    def pop(self):
        dele = self.data.pop()
        mid = dele
        self.data[0] = mid
        i = 0
        l = 2 * i + 1
        r = 2 * i + 2
        left = self.data[l]
        right = self.data[r]
        while l < len(self.data):
            if r < len(self.data):
                if mid.prior < left.prior or mid.prior < right.prior:
                    if left.prior > right.prior:
                        self.data[i] = left
                        self.data[l] = mid
                        i = l
                    else:
                        self.data[i] = right
                        self.data[r] = mid
                        i = r
                    r = 2 * i + 2
                    l = 2 * i + 1
                    if r < len(self.data):
                        right = self.data[r]
                    if l < len(self.data):
                        left = self.data[l]
                else:
                    break

            else:
                if mid.prior < left.prior:
                    self.data[i] = left
                    self.data[l] = mid
                else:
                    break

        return dele

        # 把末尾元素覆盖到头部，在删除末尾元素
        # 比较该元素和两个子元素的优先级
        # 如果有子元素优先级高于该元素，则交换父子位置

    def top(self):
        return self.data[0]


pri = heap()
a = node(5, 5)
b = node(3, 3)
c = node(4, 4)
d = node(1, 1)
e = node(2, 2)
f = node(0, 0)
g = node(9, 9)
pri.add(a)
pri.add(b)
pri.add(c)
pri.add(d)
pri.add(e)
pri.add(f)
print(pri)
pri.add(g)
print(pri)
pri.pop()
print(pri)
