# 百分号 %
num = 0.75
print("百分数是：%.2f%%" % (num * 100))

# format() 函数
print("{num}".format(num=num))

# f-strings
print(f"{1 + 2}")
print(f"{'a' + 'b'}")

# 宽度
number = 123.456
print(f"{number:10}")
print(f"{number:010}")
print(f"{number:.2f}")
