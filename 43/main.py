# 由关系遍历
# 以有向图为例

# 虽然我们可以通过graph的node属性很容易的遍历mode
# 但事实上，我们往往需要通过“关系”来遍历

class graph:
    def __init__(self, collect):
        self.collect = collect

        for x in self.collect:
            self.node.append(x)

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
            # 以下是一个比 多次remove 更好的算法
            for i in range(len(self.collect[fnode]) - 1, -1, -1):
                if self.collect[fnode][i] == node:
                    self.collect[fnode].pop(i)

    def dfs(self):
        node = self.node.copy()
        res = []

        def do(head):
            node.remove(head)
            res.append(head)
            li = self.collect[head]

            for tail in li:
                if tail in node:
                    do(tail)

        while node:
            head = node[0]
            do(head)
        return res

    def bfs(self):
        node = self.node.copy()
        res = []
        while node:

            queue = [node[0]]

            while queue:
                cur = queue.pop(0)

                res.append(cur)
                node.remove(cur)

                li = self.collect[cur]
                for tail in li:
                    if (tail in node) and (tail not in queue):
                        queue.append(tail)

        return res



# 有权图 7.5 G7
collect = {
    "a": ["c", "d"],
    "b": ["a", "c", "f"],
    "c": ["b", "e"],
    "d": ["e"],
    "e": ["g"],
    "f": ["g"],
    "g": []
}
gra = graph(collect)

dfs = gra.dfs()
print(dfs)
print()

bfs = gra.bfs()
print(bfs)