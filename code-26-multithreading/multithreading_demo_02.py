from random import randint
from time import time, sleep
from multiprocessing import Process


def download_task(filename):
    print(f"开始下载{filename}...")
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print(f"{filename}下载完成! 耗费了{time_to_download}秒")


# 单线程下载
def main():
    start = time()
    p1 = Process(target=download_task, args=('Python从入门到住院.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Peking Hot.avi',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f"总共耗费了{end - start}秒.")


if __name__ == "__main__":
    main()
