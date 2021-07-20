# 内置的collection包
# 从deque到collection

import collections

# deque
# 双端队列
# 或可代替 stack 和 queue
b = ['a', 'b', 'c']
q = collections.deque(b)
q.appendleft('xxx')
print(list(q))
q.popleft()
print(list(q))
q.extendleft([1,2,3])
print(q)
# extend填入是反向的
# 使我们可以高效的在开头添加/删除数据


# namedtuple
a = ('x', 'y', 'r')
circle = collections.namedtuple('CIRCLE', a)
p = circle(1, 2, 3)  # 创建
print(p)
print(p.r)
# 为元组命名使我们可以用名称来引用数据
# 同时规定内部数据个数
# 相当于一个mini类


# defaultdict
r = collections.defaultdict(lambda: 'NONONONONONONONNO')
r['0'] = 976
print(r['0'])
print(r['1'])
# 访问未定义的key时返回给出的结果
# 可惜的属性是只能后续添加

# OrderedDict
od = collections.OrderedDict({'1': 11, '2': 22, '3': 33})
od['0'] = 00
od['1'] = 111111
od['4'] = 44
print(dict(od))
listofod = list(od.keys())
# 按插入顺序返回key
for x in listofod:
    print(od[x], end='   ')
print()
# 顺序返回value

# 计数器
co_base = [1, 1, 1, 2, 3, 1, 2, 'a', 'A', True, True, None, None, False, False, 'asfdafd']
co = collections.Counter(co_base)
print(dict(co))
# true记为1，false记为0