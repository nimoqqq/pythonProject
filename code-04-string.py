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
