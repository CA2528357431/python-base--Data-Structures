# 括号匹配

class stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        x = self.data[len(self.data) - 1]
        self.data.pop()
        return x

    def top(self):
        return self.data[len(self.data) - 1]

    def empty(self):
        if self.data:
            return False
        else:
            return True

def do(lang):
    sta = stack()
    result = []
    for x in range(0,len(lang)):
        if lang[x] == "(":
            sta.push(x)
        elif lang[x] == ")" and sta.empty() == False:
            print(x)
            tup = (sta.pop(),x)
            result.append(tup)
    return result

lang = "()1984 (good(and)fiction(where to (go) 6.4) op)   )(asd(o)"
res = do(lang)
print(res)






