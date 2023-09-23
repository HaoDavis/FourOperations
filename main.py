from Outcome import Outcome
from Generator import Generator
import argparse
import time

import os


def main():
    start = time.time()
    # 输入文件绝对路径，arg1，arg2为要查重的文件，arg3为答案文件
    parser = argparse.ArgumentParser(description="四则运算生成器")
    parser.add_argument('-n', default=10000, type=str, help='生成题目的个数')
    parser.add_argument('-r', default='10', type=str, help='生成题目中数值的范围')
    parser.add_argument('-e', type=str, default=" ", help='题目文件')
    parser.add_argument('-a', type=str, default=" ", help='答案文件')
    args = parser.parse_args()
    # 把r限制在自然数范围内
    # 使用异常处理来确保r是一个数字
    try:
        if int(args.r)>0:
            pass
    except TypeError:
        print("请输入一个自然数")
    except ValueError:
        print("请输入一个自然数")
    # try:
    #     try:
    #         if args.r > 0:
    #             pass
    #         else:
    #             print(f"{args.r} 不是自然数（正整数）")
    #     except TypeError:
    #         print("请输入一个数")
    # except ValueError:
    #     print("输入不是有效的整数")

    n, r, e, a = int(args.n), int(args.r), args.e.strip(), args.a.strip()
    product = Generator(r, n)
    questions = product.problemArray
    # 存储生成的表达式，存进 ： “Exercises.txt”
    answer = Outcome()
    answer.expression_result(questions)  # 生成题目的答案、

    if os.path.exists(e) and os.path.exists(a):
        print("核对答案")
        answer.check_result(e, a)

    end = time.time()
    print("程序运行时间：{}s".format(end - start))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
