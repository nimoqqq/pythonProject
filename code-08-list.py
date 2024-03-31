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