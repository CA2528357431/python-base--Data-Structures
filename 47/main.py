# dijkstra

# 有向加权图
# 权重为正

# 一点到其他点最短路径

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
                edge.append(((fnode, lnode), weight))
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
            for i in range(len(self.collect[fnode]) - 1, -1, -1):
                if self.collect[fnode][i][0] == node:
                    self.collect[fnode].pop(i)


def dijkstra(gra: graph, dic: dict):
    edges = []
    for node in dic:
        neoedges = gra.outedgesofnode(node)
        edges.extend(neoedges)
    for edge in edges:
        fnode = edge[0][0]
        lnode = edge[0][1]
        weight = edge[1]
        if (lnode not in dic) or (dic[lnode] > weight + dic[fnode]):
            dic[lnode] = weight + dic[fnode]
            break
    return dic

collect = {
    "a": [("c", 5), ("d", 2)],
    "b": [("a", 11), ("c", 4), ("f", 4)],
    "c": [("b", 3), ("e", 2), ("f", 7)],
    "d": [("e", 6)],
    "e": [("g", 2)],
    "f": [("g", 3)],
    "g": [],
    "h": []
}

map = graph(collect)
start = "a"
ori = {start: 0}

res = dijkstra(map, ori)
i = 0
while len(res) != i:
    i += 1
    res = dijkstra(map, ori)

for x in collect:
    if x not in res:
        res[x] = -1

print(res)


