# 邻接矩阵表示无向图

# 点太多会有大量空白数据


class graph:
    def __init__(self, name, square):
        self.node = name
        self.square = square

    @property
    def edge(self):
        edge = []
        for y in range(0, len(self.square)):
            for x in range(y, len(self.square)):
                if self.square[y][x] != 0:
                    xn = self.node[x]
                    yn = self.node[y]
                    edge.append((yn, xn))
        return edge

    def edgesofnode(self, node):
        res = []
        for edge in self.edge:
            if node in edge:
                res.append(edge)
        return res

    def degree(self, node):
        res = self.edgesofnode(node)
        return len(res)


# 无向图 7.3 G6

square = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

name = ["a", "b", "c", "d"]
# 可以用矩阵乘方来求 路径长为若干的、某到某的路径的数量，并可以此求可达矩阵
# 对角线、无边时选择 0 还是 ∞ 根据情况选择

gra = graph(name,square)

print(gra.edge)

degree = gra.degree("b")
print(degree)

egde = gra.edgesofnode("b")
print(egde)