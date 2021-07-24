# 哈夫曼编码

# Huffman Tree

# 为每个 字符 产生一个唯一的二进制编码
# 二进制编码分配与字符出现次数有关，本算法使得整个文段所需二进制编码最短
# 编码的前任意位组成的“编码”不能表示任何一个字符（不会混淆）


# 以字符出现次数为权重

import collections

class tree:

    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
        self.code = None
        self.data = None

    @property
    def lisp(self):
        lisp = [(self.data, self.root), None, None]
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
            res.append((x.data, x.root))
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


def do(msg: dict):
    li = heap()
    for data, weight in msg.items():
        y = tree(weight)
        y.data = data
        li.add(y)
    while len(li.data) > 1:
        x = li.pop()
        y = li.pop()
        temp = tree(x.root + y.root, x, y)
        li.add(temp)
    return li.top()


def setcode(tre: tree):
    tre.code = ""

    res = {}
    def set(tre):
        if tre.left is not None or tre.right is not None:
            if tre.left is not None:
                tre.left.code = tre.code + "0"
                set(tre.left)
            if tre.right is not None:
                tre.right.code = tre.code + "1"
                set(tre.right)
        else:
            res[tre.data] = tre.code
    set(tre)

    return res

string = "eaaabbbcdcdddadaaba"
msg = collections.Counter(string)
print(msg)

res = do(msg)
print(res)

codes = setcode(res)
print(codes)
