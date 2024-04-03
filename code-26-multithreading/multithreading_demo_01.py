from random import randint
from time import time, sleep

def download_task(filename):
    print(f"开始下载{filename}...")
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print(f"{filename}下载完成! 耗费了{time_to_download}秒")

# 单线程下载
def main():
    start = time()
    download_task('Python从入门到住院.pdf')
    download_task('Peking Hot.avi')
    end = time()
    print(f"总共耗费了{end - start}秒.")


if __name__ == "__main__":
    main()
