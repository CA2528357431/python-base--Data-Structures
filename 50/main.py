# AOV

# 有向图

# 常用于表示“先决关系”
# 用点表示时间
# 若有边<a,b>
# 则要求a是b的先决条件

# 必然无回路，否则自己是自己的先决条件，deadlock

# 求一个顺序

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
            for i in range(len(self.collect[fnode]) - 1, -1, -1):
                if self.collect[fnode][i] == node:
                    self.collect[fnode].pop(i)

    @property
    def zerodegree(self):
        zero = [x for x in self.node if self.indegree(x) == 0]
        return zero


def aov(origra: graph):
    gra = graph(origra.collect.copy())
    # 维护原graph
    res = []
    while len(res) < len(origra.node):
        node = gra.zerodegree[0]
        res.append(node)
        gra.removenode(node)
    return res


# 7.12

dic = {
    "a1": ["a3", "a4", "a5"],
    "a2": ["a3", "a6"],
    "a3": ["a6", "a7", "a8", "a9"],
    "a4": ["a6", "a7", "a8", "a10"],
    "a5": ["a7"],
    "a6": ["a8"],
    "a7": ["a9", "a10"],
    "a8": ["a9", "a10"],
    "a9": [],
    "a10": []
}

gra = graph(dic)

x = aov(gra)

print(x)
