# prim


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

    def prim(self):
        origin = self.node[0]
        origincollect = {origin: []}
        gra = graph(origincollect)

        while len(gra.node)<len(self.node):
            edges = []
            for node in gra.node:
                li = self.edgesofnode(node)
                edges.extend(li)
            edges.sort(key=lambda x: x[1])
            for edge in edges:
                fnode = edge[0][0]
                lnode = edge[0][1]
                weight = edge[1]

                if fnode in gra.node and lnode in gra.node:
                    continue
                else:
                    if fnode in gra.node:
                        gra.addnode(lnode)
                    else:
                        gra.addnode(fnode)
                    gra.addedge(fnode, lnode, weight)
                    break

        return gra

collect = {
    "a": [("b", 5), ("c", 11), ("d", 5)],
    "b": [("a", 5), ("d", 3), ("e", 9), ("g", 7)],
    "c": [("a", 11), ("d", 7), ("f", 6)],
    "d": [("a", 5), ("b", 3), ("c", 7), ("g", 20)],
    "e": [("b", 9), ("g", 8)],
    "f": [("c", 6), ("g", 8)],
    "g": [("b", 7), ("d", 20), ("e", 8), ("f", 8)]
}

gra = graph(collect)

neogra = gra.prim()

print(neogra)