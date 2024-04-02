from random import randint


# 入参设置默认值
def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))


# 在参数名前面的*表示args是一个可变参数
def add1(*args):
    total = 0
    for val in args:
        total += val
    return total


print(add1())
print(add1(1))
print(add1(1, 2))
print(add1(1, 2, 3))
print(add1(1, 3, 5, 7, 9))
