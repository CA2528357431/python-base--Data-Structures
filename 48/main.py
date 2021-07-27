# floyd

# 求任一点到其他点的距离
# 对有向、无向加权图都可
# 以有向加权为例

# https://www.cnblogs.com/wangyuliang/p/9216365.html

class graph:
    def __init__(self, name, square):
        self.node = name
        self.square = square

    def __str__(self):
        reli = []
        for x in self.square:
            re = ""
            for y in x:
                yy = str(y)
                yyy = yy.ljust(4)
                re += yyy
            reli.append(re)
        res = "\n".join(reli)
        return res

    @property
    def edge(self):
        edge = []
        for y in range(0, len(self.square)):
            for x in range(0, len(self.square)):
                if self.square[y][x] != 0:
                    xn = self.node[x]
                    yn = self.node[y]
                    weight = self.square[y][x]
                    edge.append(((yn, xn), weight))
        return edge

    def edgesofnode(self, node):
        res = []
        for edge in self.edge:
            if node in edge[0]:
                res.append(edge)
        return res

    def inedgesofnode(self, node):
        res = []
        for edge in self.edge:
            if node == edge[0][1]:
                res.append(edge)
        return res

    def outedgesofnode(self, node):
        res = []
        for edge in self.edge:
            if node == edge[0][0]:
                res.append(edge)
        return res

    def degree(self, node):
        res = self.edgesofnode(node)
        return len(res)

    def indegree(self, node):
        res = self.inedgesofnode(node)
        return len(res)

    def outdegree(self, node):
        res = self.outedgesofnode(node)
        return len(res)

    def addedge(self, p1, p2, weight):
        y = self.node.index(p1)
        x = self.node.index(p2)
        self.square[y][x] = weight

    def removeedge(self, p1, p2):
        y = self.node.index(p1)
        x = self.node.index(p2)
        self.square[y][x] = 0


def floyd(map: graph):
    square = map.square.copy()
    length = len(square)
    for i in range(0, length):
        for y in range(0, length):
            for x in range(0, length):
                if (square[y][x] == 0 and y != x) or (square[y][x] > square[y][i] + square[i][x]):
                    # 如果不用0而用一个大数代表无连接，则(square[y][x] == 0 and y != x)可省
                    square[y][x] = square[y][i] + square[i][x]
    return square


# 对于i的遍历，相当于允许以某为中介 x->y = x->i and i->y
# 随着i增加，允许作为中介的点也增加


square = [
    [0, 2, 6, 4],
    [0, 0, 3, 0],
    [7, 0, 0, 1],
    [5, 0, 12, 0]
]
name = ["a", "b", "c", "d"]
gra = graph(name, square)

res = floyd(gra)
print(res)
