# AOE

# 有向加权图

# 以点表示瞬间事件
# 以边表示改变状态的活动
# 只有一个点的全部入度都实现才能转变事件
# 亦无回路
# 全图只有一个起点入度为0
# 全图只有一个终点出度为0

# 每个状态的多个活动可以同时发生

# 求总时间最长的回路————关键路、总时间、各事件最早发生时间、最晚无影响时间

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

    @property
    def ee(self):
        start = list(enumerate(self.collect))[0][1]
        ee = {start:0}
        nodes = [start]
        while len(nodes)<len(self.node):
            edges = []
            for fnode in nodes:
                li = self.outedgesofnode(fnode)
                edges.extend(li)
            for edge in edges:
                fnode = edge[0][0]
                lnode = edge[0][1]
                weight = edge[1]
                if (lnode not in ee) or (ee[lnode] < ee[fnode]+weight):
                    ee[lnode] = ee[fnode]+weight
                    if lnode not in nodes:
                        nodes.append(lnode)

        return ee

    @property
    def le(self):
        last = list(enumerate(self.collect))[-1][1]
        le = {last:self.ee[last]}
        nodes = [last]
        while len(nodes)<len(self.node):
            edges = []
            for lnode in nodes:
                li = self.inedgesofnode(lnode)
                edges.extend(li)
            for edge in edges:
                fnode = edge[0][0]
                lnode = edge[0][1]
                weight = edge[1]
                if (fnode not in nodes) or (le[fnode] > le[lnode] - weight):
                    le[fnode] = le[lnode] - weight
                    if fnode not in nodes:
                        nodes.append(fnode)


        return le


# 7.14

collect = {
    "v0": [("v1", 7), ("v2", 13), ("v3", 8)],
    "v1": [("v2", 4), ("v5", 14)],
    "v2": [("v4", 5), ("v6", 8), ("v7", 12)],
    "v3": [("v4", 13), ("v7", 10)],
    "v4": [("v5", 7), ("v6", 3)],
    "v5": [("v8", 5)],
    "v6": [("v8", 7)],
    "v7": [("v8", 8)],
    "v8": []
}

gra = graph(collect)

ee = gra.ee
le = gra.le

print(ee)
print(le)