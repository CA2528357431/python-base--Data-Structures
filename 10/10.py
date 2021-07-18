# 定和问题

def do(li,tar):

    if len(li)>1:
        li0 = li.copy()
        x = li0[0]
        li0.pop(0)
        res = do(li0,tar)
        res1 = do(li0,tar-x)
        for sol in res1:
            sol.append(x)
        res.extend(res1)
        return res
    else:
        if tar == li[0]:
            return [li]
        elif tar == 0:
            return [[]]
        else:
            return []

li = [1,2,3,4,5,6]
tar = 6
res = do(li,tar)
print(res)