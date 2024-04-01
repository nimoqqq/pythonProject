# 字典 dict

dict1 = {'one': 1, 'two': 2}
print(dict1)

dict2 = dict(one=1, two=2)
print(dict2)

dict3 = {x: x ** 2 for x in range(10)}
print(dict3)

# 作业
list_name = ['name1', 'name2', 'name3']
list_sn = [1111, 2222, 3333]
name_sn = dict(zip(list_name, list_sn))
print(name_sn)

# 常见操作
mail_list = {'tom': 'tom@gmail.com', 'jerry': 'jerry@gmail.com', 'john': 'john@163.com'}
print(mail_list.items())
print(mail_list.keys())
print(mail_list.values())
print(mail_list.get('tom'))
print(len(mail_list))

# 遍历字典
print("遍历字典:")
for key, value in mail_list.items():
    print(f"{key} : {value}")

# 添加默认 value
tom_mail = mail_list.setdefault("tom2", "tom2@163.com")
print(tom_mail)
print(mail_list)

# 添加
mail_list['wilson'] = 'wilson@163.com'

print(len(mail_list))
print(mail_list.pop('wilson'))
# 移除最后一个元素
print(mail_list.popitem())
print(len(mail_list))

new_mail_list = {'tom': 'tom_xx@gmail.com', 'jerry': 'jerry_xx@gmail.com', 'john': 'john@163.com'}
mail_list |= new_mail_list  # 使用新字典替换
print(mail_list)
