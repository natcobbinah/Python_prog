from custom_stack import Stack

stack = Stack()

math_expr = "( 1 + 2 ) * 3"

# rank function to determine operator precedence


def rank(term):
    if term == "*" or term == "/":
        return 2
    elif term == "+" or term == "-":
        return 1
    elif term == "(":
        return 0
    else:
        return -1


def toPostfix(expr):
    postfix_expr = ""
    space = " "  # space is used to separate each operator or operand in final expr

    for term in expr:
        if rank(term) == 0:
            stack.push(term)
        elif term == ")":
            while not stack.isEmpty() and rank(stack.peek()) > 0:
                postfix_expr += space
                postfix_expr += stack.pop()
            stack.pop()
        elif rank(term) > 0:
            while not stack.isEmpty() and rank(stack.peek()) >= rank(term):
                postfix_expr += space
                postfix_expr += stack.pop()
            stack.push(term)
        else:
            postfix_expr += term

    # add any remaining operator on stack to expression
    while not stack.isEmpty():
        postfix_expr += space
        postfix_expr += stack.pop()

    return postfix_expr


#print(toPostfix(math_expr))  # 1 2 + 3 *
