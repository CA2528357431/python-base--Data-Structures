# 迷宫问题--回溯


def do(ma, start):
    x, y = start
    used = [start]
    res = []
    def next(x,y,used):
        neo = used.copy()
        # li可变类型，若直接append（used）已经加入res的结果还会变
        if (x != 0 and x != ma.x and y != 0 and y != ma.y) or (x==start[0] and y==start[1]):
            for xx,yy in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if ((xx,yy) not in neo) and ma.data[yy][xx] == 1:
                    neo.append((xx,yy))
                    next(xx,yy,neo)
                    neo.pop()

        else:
            res.append(neo)

    next(x,y,used)

    return res




class pa:
    def __init__(self):
        self.data = None
        self.size = 0
ma = pa()
ma.data = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
ma.x = 11
ma.y = 11
start = (0, 10)

res = do(ma, start)
for x in res:
    print(x)