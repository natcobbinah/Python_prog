from collections import deque
import re


class Stack:

    def __init__(self):
        self.elements = deque([])

    def push(self, item):
        self.elements.append(item)

    def peek(self):
        if self.elements:
            return self.elements[-1]
        else:
            return None

    def pop(self):
        return self.elements.pop()

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return len(self.elements) == 0


class Solution:

    def cleanExpression(self, expression):
        final_expr = ""
        expression = expression.replace(" ", "")
        i = 0

        while i < len(expression):
            if (expression[i] == "+" or expression[i] == "-"):
                if (i == 0 or expression[i - 1] == "("):
                    final_expr += '0'
            final_expr += expression[i]
            i += 1
        return final_expr

    def tokenize(self, code):
        tokenized_mathExpression = []

        token_specification = [
            ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
            ('OP',       r'[+\-*/]'),      # Arithmetic operators
            ('BRACKET_OPEN',  r'\('),         # Open Parentheses
            ('BRACKET_CLOSED',  r'\)')          # Closed Parentheses
        ]

        tok_regex = '|'.join('(?P<%s>%s)' %
                             pair for pair in token_specification)

        for mo in re.finditer(tok_regex, code):
            kind = mo.lastgroup
            value = mo.group()

            if kind == 'NUMBER':
                value = float(value) if '.' in value else int(value)
            tokenized_mathExpression.append(value)
        return tokenized_mathExpression

    def rank(self, math_operator):
        if math_operator == "*" or math_operator == "/":
            return 2
        if math_operator == "+" or math_operator == "-":
            return 1
        if math_operator == "(":
            return 0
        else:
            return -1

    def toPostfix(self, math_expression):

        stack = Stack()
        postfix_expr = ""
        space = " "

        # clean expression to cater for leading - or + before operands
        cleaned_math_expression = self.cleanExpression(math_expression)
        tokenized_math_expression = self.tokenize(cleaned_math_expression)

        for term in tokenized_math_expression:
            if self.rank(term) == 0:
                stack.push(term)
            elif term == ")":
                while not stack.isEmpty() and self.rank(stack.peek()) > 0:
                    postfix_expr += space + str(stack.pop())
                stack.pop()
            elif self.rank(term) > 0:
                while not stack.isEmpty() and self.rank(stack.peek()) >= self.rank(term):
                    postfix_expr += space + str(stack.pop())
                stack.push(term)
            else:
                postfix_expr += space + str(term)

        # add any remaining operator on stack to expression
        while not stack.isEmpty():
            postfix_expr += space + stack.pop()

        return postfix_expr

    def calc(self, term, lhs_operand, rhs_operand):
        if term == "+":
            return lhs_operand + rhs_operand
        if term == "-":
            return lhs_operand - rhs_operand
        if term == "*":
            return lhs_operand * rhs_operand
        if term == "/":
            return lhs_operand / rhs_operand

    def evalPostfix(self, mathExpression):
        stack = Stack()
        final_result = ""

        for term in mathExpression.split():
            if term in ('+ - * /'):
                rhs_operand = stack.pop()
                lhs_operand = stack.pop()
                result = self.calc(term, int(lhs_operand), int(rhs_operand))
                stack.push(result)
            else:
                stack.push(term)

        # should in case only operand with no operators are keyed as input
        if stack.size() > 1:
            while not stack.isEmpty():
                final_result += stack.pop()
            return int(final_result[::-1])
        else:
            return int(stack.pop())

    def calculate(self, s: str) -> int:
        postfix_expression = self.toPostfix(s)
        return self.evalPostfix(postfix_expression)


s = Solution()
eg1 = "1- ( -2)"
eg2 = "1 - 11"
eg3 = "4 + 7"
eg4 = "3+2*2"
print(s.calculate(eg1))
