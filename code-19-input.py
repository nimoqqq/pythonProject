# 交互式 input
import argparse

text = input("请输入控制台指令")
print(text)
# 非交互式输入

parser = argparse.ArgumentParser(description="描述程序的用途")
# parser.add_argument("需要添加的参数和参数描述")
# parser.add_argument("-number", help="输入一个数字")  # -number 可选参数
parser.add_argument("number", type=int, default=10, help="请输入一个数字")  # number 必选参数
args = parser.parse_args()  # args 用于接收参数并进行处理
print(args.number)
