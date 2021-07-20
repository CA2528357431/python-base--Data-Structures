# 递归应用---八皇后


def do(n):
    queen = []
    linep = []
    linem = []
    res = []
    def add():
        if len(queen)==n:
            reque = queen.copy()
            res.append(reque)
        else:
            cur = len(queen)
            for x in range(0,n):
                if x not in queen and x+cur not in linep and x-cur not in linem:
                    queen.append(x)
                    linem.append(x-cur)
                    linep.append(x+cur)
                    add()
                    queen.pop()
                    linem.pop()
                    linep.pop()
    add()
    return res

res = do(8)
for x in res:
    print(x)
print(len(res))


