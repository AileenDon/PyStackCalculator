# Translate infix into prefix expressions
def infix_to_prefix(expression):
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def reverse_expression(expr):
        # Reverse the expression
        expr = expr[::-1]
        expr = expr.replace('(', 'temp').replace(')', '(').replace('temp', ')')
        return expr

    def handle_unary_minus(expr):
        # Convert negative sign to '^'
        new_expr = []
        for i, char in enumerate(expr):
            if char == '-' and (i == 0 or expr[i - 1] == "("):
                new_expr.append('^')
            else:
                new_expr.append(char)
        return ''.join(new_expr)

    def infix_to_prefix_process(expr):
        stack = []
        output = []
        for char in expr:
            if char.isalpha() or char.isdigit():
                output.append(char)
            elif char == '(':
                stack.append('(')
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack: stack.pop()
            else:
                while stack and precedence(char) < precedence(stack[-1]):
                    output.append(stack.pop())
                stack.append(char)
        while stack:
            output.append(stack.pop())
        return ''.join(output)

    # Process the expression
    reverse_expr = infix_to_prefix_process(reverse_expression(handle_unary_minus(expression)))
    prefix = reverse_expression(reverse_expr)
    return prefix


# Test the infix_to_prefix function
infix = "-b"
prefix_expression = infix_to_prefix(infix)
print(f"Infix: {infix}")
print(f"Prefix: {prefix_expression}")


# Extra Credits: check the balances of the parenthesis
def check_parentheses_balance(expr):
    stack = []
    for char in expr:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


# Check the check_parentheses_balance function
if check_parentheses_balance(infix):
    print(f"The expression '{infix}' has balanced parentheses.")
else:
    print(f"Error: The expression  '{infix}' has unbalanced parentheses.")

expression = "(-a + b))"
if check_parentheses_balance(expression):
    print(f"The expression '{expression}' has balanced parentheses.")
else:
    print(f"Error: The expression  '{expression}' has unbalanced parentheses.")
