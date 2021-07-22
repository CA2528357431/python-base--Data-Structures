import heapq

# 创建heapq对象
ak = [1, 9, 4, 5, 0, 2, 8]
heapq.heapify(ak)
print(ak)
print()

# 弹出最小值
x = heapq.heappop(ak)
print(ak)
print(x)
print()

# 添加值
heapq.heappush(ak, 3)
print(ak)

# 弹出最小后推入新值
# poppush
y = heapq.heapreplace(ak, 3)
print(ak)
print(y)
print()

# 推入新值后弹出最小
z = heapq.heappushpop(ak, 1)
print(ak)
print(z)
print()

# 堆的前若干个最 大/小 的数据
li1 = heapq.nsmallest(3, ak)
print(li1)
li2 = heapq.nlargest(3, ak)
print(li2)

# dic 用key指定排序依据后取值前几
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(heapq.nlargest(2, list2, key=lambda tar: tar['shares']))
print(heapq.nsmallest(2, list2, key=lambda tar: tar['shares']))
