# 通信录
import pprint
from tinydb import TinyDB

db = TinyDB('./file/db.json')  # 指定存放通讯录的文件

with open("./file/address_book.csv") as f:
    csv_data = f.readlines()
    pprint.pprint(csv_data)

friend_1 = {'name': csv_data[0].split(',')[1], 'source': csv_data[0].split(',')[2], 'tel': csv_data[0].split(',')[3]}
friend_2 = {'name': csv_data[1].split(',')[1], 'source': csv_data[1].split(',')[2], 'tel': csv_data[1].split(',')[3]}
friend_3 = {'name': csv_data[2].split(',')[1], 'source': csv_data[2].split(',')[2], 'tel': csv_data[2].split(',')[3]}

# 插入数据库
db.insert_multiple([
    friend_1, friend_2, friend_3
])

# 查询所有
print(db.all())




# 读取文件示例
# with open("./file/demo.txt") as f:
#     file_data = f.readlines()
#     pprint.pprint(file_data)
# # 统计所有行
# print(len(file_data))
# # 统计空行
# print(file_data.count("\n"))
# # 统计非空行
# print(len(file_data) - file_data.count("\n"))
# # 使用 set 特性处理重复的 '\n'
# print(len(set(file_data)) - 1)
#
# # 统计 of 出现的次数
# print(str(file_data).split(" ").count('of'))
