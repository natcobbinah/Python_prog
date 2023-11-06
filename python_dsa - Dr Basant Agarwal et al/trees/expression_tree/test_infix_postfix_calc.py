from expr_infix_toPostfix_stacks import toPostfix
from expr_tree_Postfix_stacks import evalPostfix

math_expr ="1 + 2 * 3"

postfix_expr = toPostfix(math_expr)
print(postfix_expr) # 1  2  3 * +

postfix_expr = postfix_expr.split()
result = evalPostfix(postfix_expr)
print(result) # 7
