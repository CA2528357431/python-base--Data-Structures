# 常规-->后根

# 常规求值？      先变后根周游

class stack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.empty():
            return None
        else:
            x = self.data[len(self.data) - 1]
            self.data.pop()
            return x

    def top(self):
        if self.empty():
            return None
        else:
            return self.data[len(self.data) - 1]

    def empty(self):
        if self.data:
            return False
        else:
            return True


def swap(tar):
    sta = stack()
    data = tar.split(" ")
    res = ""
    for x in data:
        if x in "()" :
            if x == "(":
                sta.push(x)
            else:
                while sta.top() != "(":
                    res += " " + sta.top()
                    sta.pop()
                sta.pop()
        elif x in "+-":
            if sta.empty():
                sta.push(x)
            elif sta.top() in "*/":
                cur = sta.pop()
                res += " " + cur
                sta.push(x)
        elif x in "*/":
            sta.push(x)
        else:
            res += " " + x
    while not sta.empty():
        cur = sta.pop()
        res += " " + cur

    return res


tar = "a + ( b + c ) * d - e"
res = swap(tar).strip()
print(res)




'''
遇到操作数，直接输出或追加到结果数组当中
遇到左括号，左括号入栈。
遇到右括号，说明这个右括号与与之匹配的左括号之间的表达式，该触发计算了，也就是应该进行转化了。遇到右括号的做法是：栈中元素出栈并且输出到结果数组当中，直到出栈的元素为左括号就停止，左括号不用输出到结果数组当中，因为后缀表达式不需要括号。
遇到运算符，栈必须满足下面三个状态中的一个，才可以将当前元素/当前运算符入栈：
4.1 如果栈为空，那么当前元素入栈；
4.2 如果栈不空，判断栈顶元素，如果栈顶元素为(，那么当前元素入栈；
4.3 如果栈不空，判断栈顶元素，如果栈顶元素的运算符优先级小，那么当前元素入栈。因为栈顶元素如果优先级小，说明其在等待后续的计算完成，栈顶这个运算符才可以完成它的计算，所以当前元素入栈就行。
如果不满足上述三个条件，那么栈的状态必然是下面这种可能：
栈不空，栈顶元素不是(，那么栈顶元素是个操作符，且优先级比当前元素高或相等，说明栈顶的这个操作符，是时候完成计算了，不需要再等当前元素了，所以栈顶元素应该出栈。之后，再继续判断栈的状态是否满足4.1、4.2、4.3这三个条件中的一个。
————————————————
版权声明：本文为CSDN博主「彭于晏湖北分晏」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/ten_sory/article/details/109624798
'''


