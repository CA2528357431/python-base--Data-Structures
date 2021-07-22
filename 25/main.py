# 堆排序

class node:
    def __init__(self, data):
        self.data = data


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
        while i >= 0 and fa.data > so.data:
            self.data[i] = so
            self.data[j] = fa
            j = i
            i = (j - 1) // 2
            so = self.data[j]
            fa = self.data[i]

    # 把新元素加到末尾
    # 只要新元素优先级高于父元素，就交换父子位置

    def pop(self):


        if len(self.data)>1:
            dele = self.data[0]
            mid = self.data.pop()
            self.data[0] = mid
            i = 0
            l = 2 * i + 1
            r = 2 * i + 2
            while l < len(self.data):
                if r < len(self.data):
                    left = self.data[l]
                    right = self.data[r]
                    if mid.data > left.data or mid.data > right.data:
                        if left.data < right.data:
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
                    left = self.data[l]
                    if mid.data > left.data:
                        self.data[i] = left
                        self.data[l] = mid
                        break
                    else:
                        break
        else:
            dele = self.data[0]
            self.data.pop()

        return dele

    def top(self):
        return self.data[0]

    def sort(self):
        res = []
        while self.data:
            x = self.pop()
            res.append(x.data)
        return res
    # 多次弹出 头元素 ,即最小元素


pri = heap()

a = node(5)
b = node(3)
c = node(4)
d = node(1)
e = node(2)
f = node(0)
g = node(9)

pri.add(a)
pri.add(b)
pri.add(c)
pri.add(d)
pri.add(e)
pri.add(f)
pri.add(g)

res = pri.sort()
print(res)

