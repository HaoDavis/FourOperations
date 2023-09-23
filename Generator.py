import random
from fractions import Fraction
from ExpressionProcess import ExpressionProcess


# 已经测试
class Generator:
    # 类变量定义
    problemArray = []  # 表达式列表表示
    exStr = ''  # 表达式字符串
    answer = 0  # 答案
    answerStr = ''  # 答案字符串
    operRange = 10  # 操作数范围
    operCount = 3  # 操作符个数
    decChance = 0.3  # 出现分数的概率
    expressionNum = 100  # 生成表达式的数目

    def __init__(self, operRange, expressionNum):  # 类的构造函数
        self.operRange = operRange
        self.operCount = 3
        decChance = random.randint(1, 30) / 100
        self.decChance = decChance
        self.expressionNum = expressionNum
        self.problemArray = self.generate_question()
        self.file_expression(self.problemArray)
        # print(self.problemArray)
        self.generated_expressions = set()  # 用于存储已生成的表达式


    def generate_question(self):
        expNum = self.expressionNum
        expressionList = []
        i = 0
        while i < expNum:
            exp = []
            #分j是奇数偶数的情况来填充运算符或操作数 从而填充完整写成表达式
            random_num_operation = random.randint(1, self.operCount)  # 运算符的数目
            number_of_oprand = random_num_operation + 1  # 操作数比操作符的数目多1
            is_need_parenteses = random.randint(0, 1)  # 是否需要加括号

            for j in range(random_num_operation + number_of_oprand):
                if j % 2 == 0:
                    exp.append(self.generate_operand()['operStr'])
                    if j > 1 and exp[j - 1] == '÷' and exp[j] == '0':
                        while True:
                            exp[j ] = self.generate_operand()
                            if exp[j ] != '0':
                                continue
                            else:
                                break
                else:
                    exp.append(self.generate_operation())
                if j > 3:
                    if exp[j - 2] == '÷' and exp[j - 1] > exp[j - 3]:
                        exp[j - 1], exp[j - 3] = exp[j - 3], exp[j - 1]
                    elif exp[j - 2] == '-' and exp[j - 1] < exp[j - 3]:
                        exp[j - 1], exp[j - 3] = exp[j - 3], exp[j - 1]
            if is_need_parenteses and number_of_oprand != 2:
                expression = " ".join(self.generate_parentheses(exp, number_of_oprand))
            else:
                expression = " ".join(exp)
            if self.expressionNum <= 500:
                if self.is_same(expressionList, expression):
                    continue
                else:
                    result = self.calculate(expression)
                    if result == "False":
                        pass
                    else:
                        expressionList.append(expression)
                        i = i + 1
            else:
                result = self.calculate(expression)
                if result == "False":
                    pass
                else:
                    expressionList.append(expression)
                    i = i + 1

        return expressionList
    def generate_operation(self):  # 随机生成操作符
        operators = ['+', '-', '×', '÷']
        return operators[random.randint(0, len(operators) - 1)]

    def generate_parentheses(self, exp, number_of_oprand):
        """
        生成括号表达式
        :param
            exp: 表达式
            number_of_oprand: 运算符数目
        :return: 括号表达式
        """
        expression = []
        num = number_of_oprand
        if exp:
            exp_length = len(exp)
            left_position = random.randint(0, int(num / 2))
            right_position = random.randint(left_position + 1, int(num / 2) + 1)
            mark = -1
            for i in range(exp_length):
                if exp[i] in ['+', '-', '×', '÷']:
                    expression.append(exp[i])
                else:
                    mark += 1
                    if mark == left_position:
                        expression.append('(')
                        expression.append(exp[i])
                    elif mark == right_position:
                        expression.append(exp[i])
                        expression.append(')')
                    else:
                        expression.append(exp[i])
        # 如果生成的括号表达式形如 (1 + 2/3 + 3) 则重新生成
        if expression[0] == '(' and expression[-1] == ')':
            expression = self.generate_parentheses(exp, number_of_oprand)
            return expression
        if expression.index(')') - expression.index('(') == 2:
            expression = self.generate_parentheses(exp, number_of_oprand)
            return expression
        return expression

    def generate_operand(self):
        # 生成获取操作数，以及是否生成分数随机判断
        operRange = self.operRange
        decChance = self.decChance

        # 用于存放返回的操作数
        result = {}
        # 若随机生成的100以内的数在概率整形内，则生成分数
        if self.rand_num(1) <= decChance:
            operArray = self.get_rand_fraction()
            result['oper'] = operArray[0] / operArray[1]  # 将分数转换为小数
            result['operStr'] = self.fraction_to_str(operArray)  # 将分数转换为字符串
            result['operArray'] = [operArray[0], operArray[1]]  # 将分数转换为数组
        else:
            oper = self.rand_num(operRange)  # 随机生成操作数
            result['oper'] = oper  # 将操作数转换为小数
            result['operStr'] = str(oper)  # 将操作数转换为字符串
            result['operArray'] = [oper, 1]  # 将操作数转换为数组
        return result

    def fraction_to_str(self, operArray):
        operNum1, operNum2 = operArray

        if operNum2 == 1:
            return operNum1

        if operNum1 > operNum2:
            temp = operNum1 // operNum2
            operNum1 -= temp * operNum2
            return f"{temp}'{operNum1}/{operNum2}"

        return f"{operNum1}/{operNum2}"

    def get_rand_fraction(self):
        operRange = self.operRange
        while True:
            operNum1, operNum2 = self.rand_num(operRange), self.rand_num(operRange)
            if operNum1 % operNum2 != 0:
                return self.to_fraction(operNum1, operNum2)

    def to_fraction(self, operNum1, operNum2):
        fraction = Fraction(operNum1, operNum2)
        return [fraction.numerator, fraction.denominator]

    def get_common_factors(self, oper):
        # 获取正整数的公因子包括其本身
        return [k for k in range(2, oper + 1) if oper % k == 0]

    def rand_num(self, range):
        # 获取随机数
        return random.randint(1, range)

    def num2symbol(self, operate):
        # 映射操作符编号到操作符符号
        operSignMap = {
            1: '+',
            2: '-',
            3: '×',
            4: '÷',
        }
        return operSignMap.get(operate, 'Invalid Operate')

    def file_expression(self, exp_list):
        if not exp_list:
            return
        with open("Exercises.txt", 'w', encoding='utf-8') as file:
            for i, exp in enumerate(exp_list):
                exp_str = f"Question{i + 1}: {exp} =\n"
                file.write(exp_str)

    def is_same(self, express_set, expression):
        """
        判断重复方法
        :param
            express_set: 表达式集合
            expression: 生成的表达式
        :return: True 或 False
        """
        # 使用哈希表来存储已生成的表达式的哈希值
        hash_set = set()

        # 计算新生成表达式的哈希值
        suffixExpression = ExpressionProcess(expression)
        target_exp_suffix = suffixExpression.re
        target_exp_hash = hash("".join(target_exp_suffix))

        # 如果哈希值已经存在于哈希集合中，表明表达式重复
        if target_exp_hash in hash_set:
            return True

        # 否则，将哈希值添加到哈希集合中，并继续检查集合中的其他表达式
        hash_set.add(target_exp_hash)

        for item in express_set:
            suffixExpression2 = ExpressionProcess(item)
            source_exp_suffix = suffixExpression2.re
            source_exp_hash = hash("".join(source_exp_suffix))

            if source_exp_hash in hash_set:
                return True

        return False

    def calculate(self, expression):  # 计算单一表达式的值
        return str(ExpressionProcess(expression).calculate_suffix())
