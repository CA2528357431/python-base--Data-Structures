# 有向有权图

# 无向有权图 即网格易做，pass


class graph:
    def __init__(self):
        self.node = []
        self.edge = []

    def addnode(self, node):
        self.node.append(node)

    def addedge(self, p1, p2, weight):
        if p1 in self.node and p2 in self.node:
            self.edge.append(((p1, p2), weight))

    def removenode(self, node):
        res = []
        if node in self.node:
            self.node.remove(node)
            for edge in self.edge:
                if node not in edge[0]:
                    res.append(edge)
        self.edge = res

    def removeedge(self, p1, p2):
        for edge in self.edge:
            if (p1, p2) in edge:
                self.edge.remove(edge)

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


# 有权图 7.3 G5

gra = graph()
for x in "abc":
    gra.addnode(x)
gra.addedge("a", "c", 5)
gra.addedge("b", "a", 7)
gra.addedge("b", "c", 2)
gra.addedge("c", "b", 3)

degree = gra.degree("b")
indegree = gra.indegree("b")
outdegree = gra.outdegree("b")
print(degree, indegree, outdegree)

egde = gra.edgesofnode("b")
inedge = gra.inedgesofnode("b")
outedge = gra.outedgesofnode("b")
print(egde, inedge, outedge)


gra.removenode("a")
degree = gra.degree("b")
indegree = gra.indegree("b")
outdegree = gra.outdegree("b")
print(degree, indegree, outdegree)


gra.removeedge("b", "c")
degree = gra.degree("b")
indegree = gra.indegree("b")
outdegree = gra.outdegree("b")
print(degree, indegree, outdegree)