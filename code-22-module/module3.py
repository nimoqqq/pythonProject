def foo():
    pass


def bar():
    pass


# 只有直接执行的模块的名字才是"__main__", 通过 import 导入并不会执行
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
