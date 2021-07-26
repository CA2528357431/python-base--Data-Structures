# 邻接表表示有向图

# 对于每个点，记录下其出边

class graph:
    def __init__(self, collect):
        self.collect = collect

    def __str__(self):
        reli = []
        for fnode in self.collect:
            re = ""
            for lnode in self.collect[fnode]:
                l = lnode.ljust(4)
                re += l
            reli.append(re)
        res = "\n".join(reli)
        return res

    @property
    def node(self):
        res = []
        for x in self.collect:
            res.append(x)
        return res

    @property
    def edge(self):
        edge = []
        for fnode in self.collect:
            for lnode in self.collect[fnode]:
                edge.append((fnode, lnode))
        return edge

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

    def addedge(self, p1, p2):
        self.collect[p1].append(p2)

    def removeedge(self, p1, p2):
        self.collect[p1].remove(p2)

    def addnode(self, node):
        self.collect[node] = []

    def removenode(self, node):
        self.collect.pop(node)
        for fnode in self.collect:

            '''
            for lnode in self.collect[fnode]:
                if lnode == node:
                    self.collect[fnode].remove(lnode)
            '''
            for i in range(len(self.collect[fnode])-1, -1, -1):
                if self.collect[fnode][i] == node:
                    self.collect[fnode].pop(i)
            # 倒叙删除可以不影响“未检查”部分的index




# 有向图 7.3 G5
collect = {
    "a":["c"],
    "b":["a", "c"],
    "c":["b"]
}

gra = graph(collect)

print(gra.edge)
print("-------")
print(gra)
print("----")
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

gra.addedge("c","a")
print("-------")
print(gra)
print("----")
print(gra.edge)
print()

gra.removeedge("c","a")
print("-------")
print(gra)
print("----")
print()

gra.removenode("c")
print("-------")
print(gra)
print("----")
print()

gra.addnode("c")
print("-------")
print(gra)
print("----")
print()