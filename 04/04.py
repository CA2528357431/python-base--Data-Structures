# KMP法

def getnext(li):
    next = [0, ]
    parser = 1
    now = 0
    while parser < len(li):
        if li[parser] == li[now]:
            now+=1
            next.append(now)
            parser += 1
        elif now == 0:
            next.append(0)
            parser+=1
        else:
            now = next[now-1]
    return next

def do(tar, che):
    i = 0
    j = 0
    next = getnext(che)
    while i < len(tar) and j < len(che):
        if tar[i] == che[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = next[j - 1]
    if j == len(che):
        return (i - len(che), i - 1)
    else:
        return ()


tar = "abcdefghijklmn"
che = "bcd"
li = do(tar, che)
print(li)

# https://www.zhihu.com/question/21923021