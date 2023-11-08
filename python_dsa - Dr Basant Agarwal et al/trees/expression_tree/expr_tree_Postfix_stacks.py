from collections import deque
import math
    
math_expr = "4 5 + 5 3 - *".split()
stack = deque([])

def calc(term, lhs_operand, rhs_operand):
    if term == "+":
        return lhs_operand + rhs_operand
    elif term == "-":
        return lhs_operand - rhs_operand
    elif term == "*":
        return lhs_operand * rhs_operand
    elif term == "/":
        return lhs_operand / rhs_operand
    elif term == "^":
        return math.pow(lhs_operand, rhs_operand)

def evalPostfix(expr):
    for term in expr:
        if term in "+ - / *  ^":
            rhs_operand = stack.pop()
            lhs_operand = stack.pop()
            result = calc(term, int(lhs_operand), int(rhs_operand))
            stack.append(result)
        else:
            stack.append(term)

    return stack.pop()


#print(evalPostfix(math_expr))


