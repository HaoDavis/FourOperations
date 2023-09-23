# -*- coding = utf-8 -*-
from fractions import Fraction


# 已经测试
class ExpressionProcess:
    """
    将中缀表达式转化为后缀表达式
    计算后缀表达式的值

    """

    exp = ""  # 中缀表达式
    re = []  # 后缀表达式
    value = 1

    def __init__(self, exp):  # 类的构造函数
        self.exp = exp
        self.re = self.mid2suffix()
        self.value = self.calculate_suffix()

    def mid2suffix(self):  # 输入是这个类的.exp属性 输出是suffix_stack栈中的内容 同时将输出放到了类的.value属性中
        """
        中缀表达式转为后缀表达式
        :param: exp: 表达式字符串
        :return: result列表
        """
        if not self.exp:
            return []
        ops_rule = {
            '+': 1,
            '-': 1,
            '×': 2,
            '÷': 2,
        }
        suffix_stack = []  # 后缀表达式结果
        ops_stack = []  # 操作符栈
        infix = self.exp.split(' ')  # 将表达式分割得到单词
        # print(infix)
        for item in infix:
            if item in ['+', '-', '×', '÷']:
                while ops_stack and ops_stack[-1] != '(' and ops_rule[item] <= ops_rule.get(ops_stack[-1], 0):
                    suffix_stack.append(ops_stack.pop())
                ops_stack.append(item)
            elif item == '(':
                ops_stack.append(item)
            elif item == ')':
                while ops_stack and ops_stack[-1] != '(':
                    suffix_stack.append(ops_stack.pop())
                ops_stack.pop()  # 弹出 '('
            else:
                suffix_stack.append(item)

        while len(ops_stack) > 0:
            suffix_stack.append(ops_stack.pop())

        self.re = suffix_stack
        return suffix_stack

    def calculate_suffix(self):
        """
        后缀表达式求值
        :return 运算结果
        """
        stack_value = []
        for item in self.re:
            # print("item")
            # print(item)
            if item in ['+', '-', '×', '÷']:
                n2 = stack_value.pop()
                n1 = stack_value.pop()
                result = self.rule(n1, n2, item)
                # print("resule:{}".format(result))
                # 求值过程中出现负数和n/0这个情况去除
                if result < 0 or result == False:
                    return False
                stack_value.append(result)
            else:
                if item.find('/') > 0:
                    attach = 0
                    right = ""
                    if item.find("'") > 0:
                        parts = item.split("'")
                        attach = int(parts[0])
                        right = parts[1]
                    else:
                        right = item
                    parts = right.split('/')
                    result = Fraction(attach * int(parts[1]) + int(parts[0]), int(parts[1]))
                    stack_value.append(result)
                else:
                    stack_value.append(Fraction(int(item), 1))

        return stack_value[0]

    def rule(self, n1, n2, op):
        if op == '+':
            return n1 + n2
        if op == '-':
            return n1 - n2
        if op == '×':
            return n1 * n2
        if op == '÷':
            if n2 == 0:
                return False
            return n1 / n2
