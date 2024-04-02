# for
friends = ["wilson", "monica", "john", "wang"]

for friend in friends:
    print(friend.capitalize())  # 首字母大写

movie1 = {"name": "Friends", "language": "En", "Sessions": "10", "Other name": "Six of One"}
for title in movie1.keys():
    print(title)

for value in movie1.values():
    print(value)

for title, value in movie1.items():
    print(f"{title} : {value}")

# 字典转枚举类型
for i in enumerate(movie1.items()):
    print(i)

# 推导式
'''
遍历元组
将遍历出的数据存入列表
'''
list1 = [i for i in (1, 2, 3, 4)]

list2 = [i * i for i in (1, 2, 3, 4)]
print(list2)

list3 = [i * i for i in (1, 2, 3, 4) if i > 2]
print(list3)
