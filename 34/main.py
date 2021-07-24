# 有向图


class graph:
    def __init__(self):
        self.node = []
        self.edge = []

    def addnode(self, node):
        self.node.append(node)

    def addedge(self, p1, p2):
        if p1 in self.node and p2 in self.node:
            self.edge.append((p1, p2))

    def removenode(self, node):
        res = []
        if node in self.node:
            self.node.remove(node)
            for edge in self.edge:
                if node not in edge:
                    res.append(edge)
        self.edge = res

    def removeedge(self, p1, p2):
        if (p1, p2) in self.edge:
            self.edge.remove((p1, p2))

    def edgesofnode(self, node):
        res = []
        for edge in self.edge:
            if node in edge:
                res.append(edge)
        return res

    def inedgesofnode(self, node):
        res = []
        for edge in self.edge:
            if node == edge[1]:
                res.append(edge)
        return res

    def outedgesofnode(self, node):
        res = []
        for edge in self.edge:
            if node == edge[0]:
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


# 7.3 G5

gra = graph()
for x in "abc":
    gra.addnode(x)
gra.addedge("a", "c")
gra.addedge("b", "a")
gra.addedge("b", "c")
gra.addedge("c", "b")

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