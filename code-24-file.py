# 文件操作
def main():
    """
    操作模式：
        r : 读取(默认)
        w : 写入
        x : 写入，如果文件已经存在会产生异常
        a : 追加
        b : 二进制
        t : 文本模式(默认)
        + : 更新(既可以读又可以写)
    """
    f = open('./file/demo.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()
