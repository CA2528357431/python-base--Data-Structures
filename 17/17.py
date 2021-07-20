# 迷宫问题--递归

def do(ma, res, start):
    neores = []
    for used in res:
        x, y = used[len(used)-1]
        if (x != 0 and x != ma.x and y != 0 and y != ma.y) or (x==start[0] and y==start[1]):

            if (x+1, y) not in used and ma.data[y][x+1] == 1:
                neoused = used.copy()
                neoused.append((x+1, y))
                neores.append(neoused)
            if (x, y+1) not in used and ma.data[y+1][x] == 1:
                neoused = used.copy()
                neoused.append((x, y+1))
                neores.append(neoused)
            if (x-1, y) not in used and ma.data[y][x-1] == 1:
                neoused = used.copy()
                neoused.append((x-1, y))
                neores.append(neoused)
            if (x, y-1) not in used and ma.data[y-1][x] == 1:
                neoused = used.copy()
                neoused.append((x, y-1))
                neores.append(neoused)
        else:
            neores.append(used)


    judge = True

    for used in neores:
        x, y = used[len(used) - 1]
        if (x != 0 and x != ma.x and y != 0 and y != ma.y) or (x==start[0] and y==start[1]):
            judge = False
            break


    if judge:
        return neores
    else:
        return do(ma,neores,start)




class pa:
    def __init__(self):
        self.data = None
        self.x = 0
        self.y = 0
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






res = do(ma,[[start]],start)
for x in res:
    print(x)

