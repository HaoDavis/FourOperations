# -*- coding = 'uft-8' -*-

import re
import os

from ExpressionProcess import ExpressionProcess


class Outcome:
    exp_list = []
    exercisefile = ""
    answerfile = ""

    def __init__(self):  # 类的构造函数
        print("创建Answer类")

    def expression_result(self, expressions):
        """
        计算表达式列表的结果并将其存储到文件中。
        :param expressions: 要评估的表达式列表。
        :return: 无
        """
        with open('Answer.txt', 'w', encoding='utf-8') as file:
            for i, exp in enumerate(expressions):
                suffix_expression = ExpressionProcess(exp)
                exp_value = suffix_expression.calculate_suffix()
                flag = float(exp_value)
                exp_value = str(exp_value)
                if '/' in exp_value and flag > 1:
                    a,b = exp_value.split('/')
                    a = int(a)
                    b = int(b)
                    # 转化成真分数
                    c = a//b
                    d = a%b
                    e = str(c)+'’'+str(d)+'/'+str(b)
                    exp_value = e
                result = f"Answer{i + 1}: {exp_value}\n"
                file.write(result)

    @staticmethod
    def check_result(exercisefile, answerfile):
        correct_list, wrong_list = [], []
        exercise_answer = []

        try:
            with open(exercisefile, 'r', encoding='utf-8') as exercise_file, \
                    open(answerfile, 'r', encoding='utf-8') as answer_file:

                for (exp_line, ans_line) in zip(exercise_file, answer_file):
                    exp_match = re.match(r'Question\d+: (.*) =\n', exp_line)
                    ans_match = re.match(r'Outcome\d+: (.*)\n', ans_line)

                    if exp_match and ans_match:
                        exp = exp_match.group(1)
                        ans = ans_match.group(1)

                        p = ExpressionProcess(exp)
                        exp_value = str(p.calculate_suffix())
                        exercise_answer.append(exp_value)

                        if ans == exp_value:
                            correct_list.append(len(correct_list) + 1)
                        else:
                            wrong_list.append(len(wrong_list) + 1)

            with open('Grade.txt', 'w+', encoding='utf-8') as grade_file:
                grade_file.write(f'Correct: {len(correct_list)} {correct_list}\n')
                grade_file.write(f'Wrong: {len(wrong_list)} {wrong_list}')
        except IOError:
            print('请检查文件路径是否正确')

if __name__ == '__main__':
    # exp_file = r'Exercises.txt'
    # ans_file = r'Outcome.txt'
    exp_file = 'Exercises.txt'
    ans_file = 'Answer.txt'
    o = Outcome()
    o.check_result(exp_file, ans_file)
