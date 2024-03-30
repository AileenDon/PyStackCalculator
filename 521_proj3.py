# Handle certain input
def check_valid_input(expr):
    expr = expr.replace(" ", "")
    
    # Check if the expression starts with an allowed unary minus
    if expr.startswith('-'):
        if len(expr) > 1 and not expr[1].isdigit() and expr[1] != '(':
            return False
    
    # Iterate through the expression to check for invalid patterns
    for i in range(1, len(expr)):
        if expr[i] in "+-*/" and expr[i-1] in "+-*/":
            if not ((expr[i] == '-' and expr[i-1] == '(') or (expr[i] == '-' and expr[i-1] == ')')):
                return False
        
        if expr[i] == '-' and not (expr[i-1] == '(' or expr[i-1] == ')' or expr[i-1].isdigit()):
            return False
            
    return True

# Translate infix into prefix expressions
def infix_to_prefix(expression):

    def reverse_expression(expr):
        # Reverse the expression
        expr = expr[::-1]
        expr = expr.replace('(', 'temp').replace(')', '(').replace('temp', ')')
        return expr
    
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

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
        # Convert the modified expression into prefix notation
        stack = []
        output = []
        for char in expr:
            if char.isalpha() or char.isdigit()or char == '^':
                output.append(char)
            elif char == '(' :
                stack.append('(')
            elif char == ')':
                while stack and stack[-1] != '(':
                    output.append(" ")
                    output.append(stack.pop())
                if stack: stack.pop()
            elif char ==' ':
                continue;
            else:
                output.append(" ")
                while stack and precedence(char) < precedence(stack[-1]):
                    output.append(stack.pop())
                stack.append(char)
        while stack:
            output.append(" ")
            output.append(stack.pop())

        return ''.join(output)

    # Process the expression
    reverse_expr = infix_to_prefix_process(reverse_expression(handle_unary_minus(expression)))
    prefix = reverse_expression(reverse_expr)
    return prefix

# Evaluate a prefix expression
def evaluate_prefix(expression):   
    stack =[]
    operators = set(['+', '-', '*', '/'])
    expression = expression.split()[::-1]  

    for token in expression:
        if token.isdigit() :
            stack.append(int(token))
        elif token.startswith('^'): 
            # Handle multiple ^ symbols 
            negation_count = len(token) - len(token.lstrip('^'))
            sign = -1 if negation_count % 2 != 0 else 1
            if token[negation_count:].isdigit():
                stack.append(sign * int(token[negation_count:]))
            else:
                raise ValueError("Invalid token in expression: " + token)
        elif token in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 // operand2  
            stack.append(result)
        else:
            raise ValueError("Invalid token in expression")

    return stack.pop()

# Check for overflow in the evaluation result
def check_overflow(result):
    if result < -128 or result > 127:
        result = (result + 128) % 256 - 128
        print("Overflow occurs!", f"Output value: {result}")
        return True  
    return False

# Evaluates it, and checks for overflow
def evaluate_expression(expression):
    result = evaluate_prefix(expression)
    if not check_overflow(result):
        return result
    else:
        return "Overflow occurred; result not valid."

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

# Ask for input, and evaluate 
def main():
    inf = input("Enter a prefix expression: ")
    if check_valid_input(inf):
        print(f"Expression '{inf}' is valid.")
        
        if check_parentheses_balance(inf):
            print(f"The expression '{inf}' has balanced parentheses.")
        else:
            print(f"Error: The expression  '{inf}' has unbalanced parentheses.")
        
        prefix_expression = infix_to_prefix(inf)
        print(f"Prefix: {prefix_expression}")

        try:
            result = evaluate_expression(prefix_expression)
            print("Result:", result)
        except (ValueError, OverflowError) as e:
            print("Error:", e)

    else:
        print(f"Expression '{inf}' is not valid. Please give a valid input.")
main()


# # Test multiple infix expressions from given doc
# expressions = [
#     "(40+50)",
#     "45+(-50)",
#     "80+80",
#     "((-36)+107)*5",
#     "(-50)-122",
#     "(-33)*3",
#     "101*61",
#     "(-101)*61",
#     "(-70)/3",
#     "(-120)/(-34)",
#     "-(-(1))",
#     "-((-(1))",
#     "-(-(1))+(-1))"
#     "-(1+2)",
#     "-1-+2",
#     "1--2",
#     "1+-2"
# ]

# for inf in expressions:
#     print("————————————————————————————")
#     if check_valid_input(inf):
#         print(f"Expression '{inf}' is valid.")
        
#         if check_parentheses_balance(inf):
#             print(f"The expression '{inf}' has balanced parentheses.")
#         else:
#             print(f"Error: The expression  '{inf}' has unbalanced parentheses.")
        
#         prefix_expression = infix_to_prefix(inf)
#         print(f"Prefix: {prefix_expression}")

#         try:
#             result = evaluate_expression(prefix_expression)
#             print("Result:", result)
#         except (ValueError, OverflowError) as e:
#             print("Error:", e)

#     else:
#         print(f"Expression '{inf}' is not valid. Please give a valid input.")
