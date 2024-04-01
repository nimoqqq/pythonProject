# 列表
colours = ["red", "blue", "green"]
print(colours)
print(type(colours))

# 字符串转换列表
print(type(list('red')))

# 循环创建列表
fList = [x for x in range(1, 10)]
print(fList)

# 访问列表
print(fList[0])
print(fList[8])
print(fList[-1])

# 二维列表
towList = ['a', 'b', [1, 2, 3]]
print(towList[2][0])

# 删除列表
del towList[0]
del towList

# 列表创建操作
list1 = ['a', 'b', 'c', 'd']
# 添加
# 指定位置插入操作
list1.insert(0, 'e')
# 最后一个元素之前插入
list1.insert(-1, 'f')
print(list1)
# 结尾插入
list1.append('g')
print(list1)
# 为列表扩展元素
list1.extend("last")
print(list1)

# 修改
# 移除列表中的元素
list1.remove('t')
print(list1)
# 反转列表元素的顺序
list1.reverse()
print(list1)
# 移除索引对应的元素
list1.pop(0)
# 复制列表
list2 = list1.copy()
print(list2)
# 清空列表
list2.clear()
print(list2)

# 统计列表长度
print(len(list1))
print(len(list1[0]))
# 元素出现的次数
print(list1.count('a'))

# 列表排序
print(list1)
list1.sort(reverse=True)
print(list1)

list3 = sorted(list1)
print(list3)
