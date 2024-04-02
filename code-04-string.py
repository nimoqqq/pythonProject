# 字符串类型

a = "字符串a"
print(a)

# 在引用的字符串中包含了 "" , 可以使用单引号来作区分
b = '字符串"b'
print(b)

# python 3.6 之后支持
x = "123"
print(f"字符串引入变量x: {x}")

# 字符串是否包含某个字符
s = "12345678"
y = "13579"
t = x in s
t1 = y not in s
print(t)
print(t1)

# 字符串拼接
xx = "abc"
yy = "xyz"
print(xx + yy)
print(xx * 3)
print(xx)
print(yy)

# 字符串切片
xxx = "1234567890"
print(xxx[3])
print(xxx[-1])
print(xxx[3:5])

# 字符串常用方法
str1 = "哈哈哈哈哈~一个非常长的字符串~哈哈哈哈哈"
print(str1.count("哈"))

str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # c12
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45
str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1))  # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize())  # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())  # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper())  # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or'))  # 8
print(str1.find('shit'))  # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He'))  # False
print(str1.startswith('hel'))  # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))  # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
