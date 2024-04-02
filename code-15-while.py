# while
number = 10
while number >= 1:
    print(f"number is {number}")
    number -= 1
    if number == 5:
        # continue # 跳过当前循环
        break  # 跳出循环

list1 = [1, 2, 3, 4, 5]
while list1:
    print(list1.pop())
