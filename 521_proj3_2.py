class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)
    
    def append(self, item):
        self.push(item)



def evaluate_prefix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])
    expression = expression.split()[::-1]  # Reverse the expression to evaluate from left to right

    for token in expression:
        if token.isdigit() :
            stack.push(int(token))
        elif token.startswith('^'): 
            stack.append(-int(token[1:]))
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
