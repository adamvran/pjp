import re
from colorama import Fore
import ast

for i in range(int(input())):
    expr = input()

    unary_found = False
    tree = ast.parse(expr, mode='eval')

    if re.match(r'^[\d+\-*/()\s]+$', expr) and '**' not in expr and '//' not in expr and '%' not in expr:
        for node in ast.walk(tree):
            if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
                print(Fore.RED + "ERROR")
                unary_found = True
                break

        if not unary_found:
            try:
                result = eval(expr)
                print(result)
            except Exception as e:
                print(Fore.RED + "ERROR", e)

        else:
            continue
    else:
        print(Fore.RED + "ERROR")
