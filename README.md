# Expression Evaluation Using a Stack-based Calculator Using Python

## Expression Parser and Prefix Converter

A utility for parsing infix arithmetic expressions and converting them to prefix notation, specifically designed for 8-bit signed integers. Includes a feature to check for balanced parentheses.

## Features

- Parses infix expressions with operators (`+`, `-`, `*`, `/`).
- Converts infix to prefix notation while handling negative numbers and operator precedence.

### Converts infix to prefix notation

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

### Evaluate prefix expression

Here are some example expressions and their results:

<img width="403" alt="Screenshot 2024-03-29 at 11 18 25 PM" src="https://github.com/AileenDon/521_proj3/assets/120889846/0afd97c6-d942-4b2b-97b1-b4efad5bf811">
<img width="392" alt="Screenshot 2024-03-29 at 11 22 27 PM" src="https://github.com/AileenDon/521_proj3/assets/120889846/afdfa1b4-159e-4c8c-86df-8276ead9b9f1">

### Overflow scenarios:

<img width="398" alt="Screenshot 2024-03-29 at 11 13 24 PM" src="https://github.com/AileenDon/521_proj3/assets/120889846/f63f993c-355f-4908-86e3-78e16812d627">

### A few assumptions concerning valid input and the handling of certain input:

<img width="425" alt="Screenshot 2024-03-29 at 11 09 25 PM" src="https://github.com/AileenDon/521_proj3/assets/120889846/43c0fdf3-8670-486d-9299-397d667bf704">

### Screenshots

<img width="238" alt="image" src="https://github.com/AileenDon/521_proj3/assets/158865231/b0075f69-f661-47d1-adac-da4e32119806">

### Extra Credits: Balanced Parentheses

The program also checks for balanced parentheses in expressions. For example:

- The expression '-b' has balanced parentheses.
- Error: The expression '(-a + b))' has unbalanced parentheses.
- Checks for balanced parentheses, outputting an error message for unbalanced expressions.

<img width="473" alt="Screenshot 2024-03-29 at 11 16 03 PM" src="https://github.com/AileenDon/521_proj3/assets/120889846/6897cead-c0f7-4d09-9359-45ac58003786">
