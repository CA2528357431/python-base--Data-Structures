# 邻接表表示无向图

# 对于每个点，记录下其出边和权

class graph:
    def __init__(self, collect):
        self.collect = collect

    def __str__(self):
        res = ""
        for fnode in self.collect:
            for lnode in self.collect[fnode]:
                l = str(lnode).ljust(14)
                res += l
            res += "\n"
        res = res[:-1]
        return res

    @property
    def edge(self):
        edge = []
        for fnode in self.collect:
            for data in self.collect[fnode]:
                edge.append(((fnode, data[0]), data[1]))
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
        self.collect[p1].append((p2, weight))

    def removeedge(self, p1, p2):
        for x in self.collect[p1]:
            if p2 == x[0]:
                self.collect[p1].remove(x)

    def addnode(self, node):
        self.collect[node] = []

    def removenode(self, node):
        self.collect.pop(node)
        for fnode in self.collect:
            for i in range(len(self.collect[fnode])-1, -1, -1):
                if self.collect[fnode][i][0] == node:
                    self.collect[fnode].pop(i)

# 有权图 7.5 G7

collect = {
    "a":[("c", 3), ("d", 6)],
    "b":[("a", 11), ("c", 4), ("f", 7)],
    "c":[("b", 3), ("e", 5)],
    "d":[("e", 5)],
    "e":[("g", 9)],
    "f":[("g", 10)],
    "g":[]
}

gra = graph(collect)

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

print("-----")
print(gra)
print("---")
print()

gra.addedge("f", "a", 24)
print("-----")
print(gra)
print("---")
print()

gra.removeedge("f", "a")
print("-----")
print(gra)
print("---")
print()

gra.removenode("c")
print("-----")
print(gra)
print("---")
print()

gra.addnode("c")
print("-----")
print(gra)
print("---")