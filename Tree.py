# -*- coding=utf-8 -*-

import operator


class Node:
    """
    二叉树的结点
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    treeStack = []  # 二叉树
    expression = []  # 表达式

    def __init__(self):
        # print("创建二叉树类")
        pass

    def generate_tree(self, exp):
        self.treeStack = []

        for item in exp:
            current_node = Node(item)

            if item not in ['+', '-', 'x', '÷']:
                self.treeStack.append(current_node)
            else:
                current_node.right, current_node.left = self.treeStack.pop(), self.treeStack.pop()
                self.treeStack.append(current_node)

        return self.treeStack[-1]

    def is_same_tree(self, root):  # 返回的是一个表示二叉树的表达式字符串
        """
        判断二叉树是否相同
        """
        if not root.left and not root.right:
            return root.value
        if root.value in ['+', '*']:
            left = self.is_same_tree(root.left)
            right = self.is_same_tree(root.right)
            return root.value + (left + right if operator.le(left, right) else right + left)
        else:  # 如果是减法和除法
            return root.value + self.is_same_tree(root.left) + self.is_same_tree(root.right)
