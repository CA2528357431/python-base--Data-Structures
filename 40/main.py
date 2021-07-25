# 邻接表表示无向图

# 对于每个点，记录下其所有边

class graph:
    def __init__(self, collect):
        self.collect = collect

    def __str__(self):
        res = ""
        for fnode in self.collect:
            for lnode in self.collect[fnode]:
                l = lnode.ljust(4)
                res += l
            res += "\n"
        res = res[:-1]
        return res

    @property
    def edge(self):
        edge = []
        for fnode in self.collect:
            for lnode in self.collect[fnode]:
                if (lnode, fnode) not in edge:
                    edge.append((fnode, lnode))
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

    def addedge(self, p1, p2):
        self.collect[p1].append(p2)

    def removeedge(self, p1, p2):
        self.collect[p1].remove(p2)

    def addnode(self, node):
        self.collect[node] = []

    def removenode(self, node):
        self.collect.pop(node)
        for fnode in self.collect:
            for i in range(len(self.collect[fnode])-1, -1, -1):
                if self.collect[fnode][i] == node:
                    self.collect[fnode].pop(i)


# 有向图 7.3 G5
collect = {
    "a":["b", "c"],
    "b":["a", "c"],
    "c":["a", "b", "d"],
    "d":["c"]
}

gra = graph(collect)

print(gra.edge)
print()

degree = gra.degree("b")
print(degree)
print()

egde = gra.edgesofnode("b")
print(egde)
print()

print(gra)
print()

gra.addedge("d","a")
print(gra)
print(gra.edge)
print()

gra.removeedge("d","a")
print(gra)