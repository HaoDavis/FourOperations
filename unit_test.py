import unittest
from ExpressionProcess import ExpressionProcess
from Generator import Generator
from main import main
from Outcome import Outcome
from Tree import Tree, Node


# 测试用例
class Case(unittest.TestCase):
    def test_mid2suffix(self):
        # 测试中缀表达式转后缀表达式
        exp = "1 + 2 + 3"
        exp_process = ExpressionProcess(exp)
        self.assertEqual(exp_process.re, ['1', '2', '+', '3', '+'])

    def test_mid2suffix2(self):
        # 测试中缀表达式转后缀表达式
        exp = "1 + 2 +"
        with self.assertRaises(IndexError):
            exp_process = ExpressionProcess(exp)

    def test_calculate_suffix(self):
        # 测试后缀表达式求值
        exp = "1 2 + 3 +"
        exp_process = ExpressionProcess(exp)
        self.assertEqual(exp_process.value, 6)

    def test_calculate_suffix2(self):
        # 测试后缀表达式求值
        exp = "1 + 2 "
        with self.assertRaises(ValueError):
            exp_process = ExpressionProcess(exp)

    def test_generate_question(self):
        # 测试生成题目
        gen = Generator(10, 10)
        question = gen.generate_question()
        self.assertEqual(len(question), 10)

    def test_generate_parentheses(self):
        # 测试生成括号
        gen = Generator(10, 10)
        question = gen.generate_parentheses("1 + 2 + 3", 2)
        self.assertEqual("(" in question, True)

    def test_mid2suffix3(self):
        # 测试中缀表达式转后缀表达式
        exp = "1 + 5 × ( 3 + 2 ) - 4 × 5"
        exp_process = ExpressionProcess(exp)
        self.assertEqual(exp_process.re, ['1', '5', '3', '2', '+', '×', '+', '4', '5', '×', '-'])

    def test_to_fraction(self):
        # 测试小数转分数
        self.assertEqual(Generator.to_fraction(self, 1, 2), [1, 2])

    def test_get_common_factors(self):
        # 测试获取公因子
        self.assertEqual(Generator.get_common_factors(self, 6), [2, 3, 6])

    def test_num2symbol(self):
        # 测试数字转符号
        self.assertEqual(Generator.num2symbol(self, 1), "+")

    def test_is_same(self):
        # 测试判断重复
        self.assertEqual(Generator.is_same(self, [], "1 + 2"), False)


if __name__ == "__main__":
    suite = unittest.TestSuite()  # 创建测试套件
    tests = [
        Case("test_mid2suffix"),
        Case("test_mid2suffix2"),
        Case("test_calculate_suffix"),
        Case("test_calculate_suffix2"),
        Case("test_generate_question"),
        Case("test_generate_parentheses"),
        Case("test_mid2suffix3"),
        Case("test_to_fraction"),
        Case("test_get_common_factors"),
        Case("test_num2symbol"),
        Case("test_is_same")
    ]
    suite.addTests(tests)  # 将测试用例加入测试套件中
    runner = unittest.TextTestRunner(verbosity=2)  # 创建测试运行器
    runner.run(suite)  # 执行测试套件
