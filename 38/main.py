# 邻接矩阵表示有向加权图

# 点太多会有大量空白数据
# 不能增加点

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


# 有权图 7.5 G7

square = [
    [0, 0, 3, 6, 0, 0, 0],
    [11, 0, 4, 0, 0, 7, 0],
    [0, 3, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0, 0, 0]
]

name = ["a", "b", "c", "d", "e", "f", "g"]

# 以上所有图，对角线、无边时选择 0 还是 ∞ 根据情况选择

gra = graph(name,square)

print(gra.edge)
print()

degree = gra.degree("b")
indegree = gra.indegree("b")
outdegree = gra.outdegree("b")
print(degree, indegree, outdegree)
print()

egde = gra.edgesofnode("b")
inedge = gra.inedgesofnode("b")
outedge = gra.outedgesofnode("b")
print(egde, inedge, outedge)
print()

print(gra)
print()

gra.addedge("f", "a", 24)
print(gra)
print()

gra.removeedge("f", "a")
print(gra)