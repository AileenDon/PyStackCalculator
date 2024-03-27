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



Enter a prefix expression when prompted and press Enter.

## Example Expressions

Here are some example expressions and their expected results:

1. `+ 10 20` => `30`
2. `- 30 10` => `20`
3. `* 5 6`   => `30`
4. `/ 20 5`  => `4`
5. `+ 10 * -3 4` => `-2`
6. `- -10 5`    => `-15`
7. `+ 10 * 2 - 6 4`  => `18`
8. `/ * 10 2 + 5 - 20 10` => `5`

## Testing

### Additional Test Cases

1. Overflow scenarios:
- `* 127 2`: Overflow error expected
- `/ -128 -2`: Overflow error expected

### Balanced Parentheses

The program also checks for balanced parentheses in expressions. For example:
- `(+ 10 (* 20 30))`: Balanced
- `(+ 10 (* 20 30)`: Unbalanced (missing closing parenthesis)
- `(+ 10 (* 20 30)) )`: Unbalanced (extra closing parenthesis)

### Screenshots


<img width="239" alt="image" src="https://github.com/AileenDon/521_proj3/assets/158865231/888ab4c1-1b1a-458d-8ac6-1c073e8c7386">

<img width="238" alt="image" src="https://github.com/AileenDon/521_proj3/assets/158865231/b0075f69-f661-47d1-adac-da4e32119806">



