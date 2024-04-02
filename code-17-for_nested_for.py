# 嵌套循环

number = 100
if number < 100:
    # pass # 空语句,待处理
    if number % 7 == 0:
        pass
    else:
        pass
else:
    pass

# 推导式
list1 = [x * x for x in range(10) if x % 7 == 0]
print(list1)

# 多重循环处理二维数组
data = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
list2 = []
for i in data:
    for j in i:
        list2.append(j)
        print(j)
print(list2)
