# Huffman Tree

class tree:

    def __init__(self, root, left=None, right=None):
        self.nodes = []
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


def do(data: list):
    li = []
    for x in data:
        y = tree(x)
        li.append(y)
    li.sort(key=lambda x: x.root)
    while len(li) > 1:
        x = li[0]
        y = li[1]
        li.pop(0)
        li.pop(0)
        temp = tree(x.root+y.root, x, y)
        li.append(temp)
        li.sort(key=lambda x: x.root)
    return li[0]

li = [7,4,2,5]
res = do(li)
print(res)