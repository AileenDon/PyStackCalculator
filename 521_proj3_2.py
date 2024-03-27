class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def evaluate_prefix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])
    expression = expression.split()[::-1]  # Reverse the expression to evaluate from left to right

    for token in expression:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()): # Checking for negative numbers
            stack.push(int(token))
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
                result = operand1 // operand2  # Integer division
            stack.push(result)
        else:
            raise ValueError("Invalid token in expression")

    return stack.pop()


def check_overflow(result):
    if result < -128 or result > 127:
        raise OverflowError("Overflow detected")


def evaluate_expression(expression):
    result = evaluate_prefix(expression)
    check_overflow(result)
    return result


def main():
    expression = input("Enter a prefix expression: ")
    try:
        result = evaluate_expression(expression)
        print("Result:", result)
    except (ValueError, OverflowError) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
