# 邻接表表示无向有权图

# 对于每个点，记录下其边和权

class graph:
    def __init__(self, collect):
        self.collect = collect

    def __str__(self):
        reli = []
        for fnode in self.collect:
            re = ""
            for (lnode, weight) in self.collect[fnode]:
                l = str(((fnode, lnode), weight)).ljust(24)
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
            for (lnode, weight) in self.collect[fnode]:
                if ((lnode, fnode), weight) not in edge:
                    edge.append(((fnode, lnode), weight))
        return edge

    def edgesofnode(self, node):
        res = []
        for edge in self.edge:
            if node in edge[0]:
                res.append(edge)
        return res

    def degree(self, node):
        res = self.edgesofnode(node)
        return len(res)

    def addedge(self, p1, p2, weight):
        self.collect[p1].append((p2, weight))
        self.collect[p2].append((p1, weight))

    def removeedge(self, p1, p2):
        for x in self.collect[p1]:
            if p2 == x[0]:
                self.collect[p1].remove(x)
        for x in self.collect[p2]:
            if p1 == x[0]:
                self.collect[p2].remove(x)

    def addnode(self, node):
        self.collect[node] = []

    def removenode(self, node):
        self.collect.pop(node)
        for fnode in self.collect:
            for i in range(len(self.collect[fnode]) - 1, -1, -1):
                if self.collect[fnode][i][0] == node:
                    self.collect[fnode].pop(i)


# 有权图 7.5 G8

collect = {
    "a": [("b", 7), ("c", 7), ("d", 9)],
    "b": [("a", 7), ("d", 3), ("g", 5), ("e", 6)],
    "c": [("a", 7), ("d", 14), ("f", 11)],
    "d": [("a", 9), ("b", 3), ("c", 14), ("g", 20)],
    "e": [("b", 6), ("g", 8)],
    "f": [("c", 11), ("g", 6)],
    "g": [("b", 5), ("d", 20), ("e", 8), ("f", 6)]
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
print(gra.node)
print("-----")
print(gra)
print("---")
print()

gra.addnode("c")
print("-----")
print(gra)
print("---")
