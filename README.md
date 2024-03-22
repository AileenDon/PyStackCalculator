# Expression Evaluation Using a Stack-based Calculator Using Python

## Expression Parser and Prefix Converter

A utility for parsing infix arithmetic expressions and converting them to prefix notation, specifically designed for 8-bit signed integers. Includes a feature to check for balanced parentheses.

### Features

- Parses infix expressions with operators (`+`, `-`, `*`, `/`).
- Converts infix to prefix notation while handling negative numbers and operator precedence.

### Test Outputs

The following table shows various infix expressions and their corresponding prefix conversions tested with the utility:

| Infix Expression  | Prefix Conversion |
| ----------------- | ----------------- |
| `-b`              | `^b`              |
| `(a + b)`         | `+ab`             |
| `(x+y-z)`         | `-+xyz`           |
| `((x+y-z)/u+v)`   | `+/-+xyzuv`       |
| `((x+y-z)/u+v*w)` | `+/-+xyzu*vw`     |
| `(-a + b)`        | `+^ab`            |
| `(x-(-y)+ z)`     | `+-x^yz`          |
| `a`               | `a`               |

Note: `^` is used to denote a unary minus for clarity in the prefix expressions.

### Usage

Modify input expression in the code for temperory easy test, will modify in the future.

## Extra Credits: Checking Parentheses Balance

Checks for balanced parentheses, outputting an error message for unbalanced expressions.

### Test Output

- The expression '-b' has balanced parentheses.
- Error: The expression '(-a + b))' has unbalanced parentheses.
