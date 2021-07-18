# stack-list

# first in last out

class stack:
    def __init__(self):
        self.data = []
    def push(self,x):
        self.data.append(x)
    def pop(self):
        x = self.data[len(self.data)-1]
        self.data.pop()
        return x
    def top(self):
        return self.data[len(self.data)-1]
    def empty(self):
        if self.data:
            return False
        else:
            return True

sta = stack()

sta.push(1)
sta.push("helo")
sta.push([9377,True])

print(sta.empty())
print(sta.pop())
print(sta.top())