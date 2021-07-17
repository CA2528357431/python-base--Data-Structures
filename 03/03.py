# 字符串匹配

tar = "abcdefghijklmn"
che = "lmn"
def do(tar,che):
    i = 0
    j = 0
    while i<len(tar) and j<len(che):
        if tar[i] == che[j]:
            i+=1
            j+=1
        else:
            i+=1
            j=0
    if j == len(che):
        return (i-len(che),i-1)
    else:
        return ()
res = do(tar, che)
print(res)