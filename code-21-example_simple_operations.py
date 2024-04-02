# 找出所有水仙花数
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

# 百钱百鸡
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + y * 3 + z / 3 == 100:
            print(f"公鸡: {x}, 母鸡: {y}, 小鸡: {z}")
