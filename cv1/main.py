import re

for i in range(int(input())):
    expr = input()
    if re.match(r'^[\d+\-*/()\s]+$', expr) and '**' not in expr and '//' not in expr and '%' not in expr:
        try:
            result = eval(expr)
            print(result)
        except Exception as e:
            print("ERROR", e)
    else:
        print("ERROR")

