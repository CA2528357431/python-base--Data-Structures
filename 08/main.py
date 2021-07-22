# 逆波兰表达式

# 后根周游


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


def do(lang: str):
    itens = lang.split(" ")
    sta = stack()

    for x in itens:
        if x == "+":
            a = sta.pop()
            b = sta.pop()
            sta.push(a + b)
        elif x == "-":
            a = sta.pop()
            b = sta.pop()
            sta.push(b - a)
            # 前面的-后面的
        elif x == "*":
            a = sta.pop()
            b = sta.pop()
            sta.push(a * b)
        elif x == "/":
            a = sta.pop()
            b = sta.pop()
            sta.push(a / b)
        else:
            sta.push(float(x))

    res = sta.pop()
    return res


lang = "5 1 2 + 4 * + 3 -"
res = do(lang)
print(res)
