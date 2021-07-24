# Huffman Tree

class tree:

    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    @property
    def lisp(self):
        lisp = [self.root, None, None]
        if self.left is not None:
            lisp[1] = self.left.lisp
        if self.right is not None:
            lisp[2] = self.right.lisp
        return lisp
        # lisp 表达法

    def __str__(self):
        return str(self.lisp)


# 用堆来存储数据
# 只需要最小，不需要排序

class heap:

    def __init__(self):
        self.data = []

    def __str__(self):
        res = []
        for x in self.data:
            res.append(x.root)
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
        while i >= 0 and fa.root > so.root:
            self.data[i] = so
            self.data[j] = fa
            j = i
            i = (j - 1) // 2
            so = self.data[j]
            fa = self.data[i]

    # 把新元素加到末尾
    # 只要新元素优先级高于父元素，就交换父子位置

    def pop(self):

        if len(self.data) > 1:
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
                    if mid.root > left.root or mid.root > right.root:
                        if left.root < right.root:
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
                    if mid.root > left.root:
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


def do(data: list):
    li = heap()
    for x in data:
        y = tree(x)
        li.add(y)
    while len(li.data) > 1:
        x = li.pop()
        y = li.pop()
        temp = tree(x.root + y.root, x, y)
        li.add(temp)
    return li.top()


li = [7, 4, 2, 5]
res = do(li)
print(res)
