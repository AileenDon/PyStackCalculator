# Expression Evaluation Using a Stack-based Calculator Using Python

This tool is designed to validate, translate, and evaluate mathematical expressions in prefix notation. It includes several features such as input validation, infix to prefix conversion, prefix expression evaluation, and overflow checking.

## Features
### Input Validation
- Function: check_valid_input(expr)
- Description: Validates the given mathematical expression to ensure it follows the correct syntax for operations and parentheses usage.

### Infix to Prefix Conversion
- Function: infix_to_prefix(expression)
- Description: Converts a mathematical expression from infix notation to prefix notation.

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

### Prefix Expression Evaluation
- Function: evaluate_prefix(expression)
- Description: Evaluates a mathematical expression provided in prefix notation and returns the result.

Here are some example expressions and their results:

<img width="403" alt="Screenshot 2024-03-29 at 11 18 25 PM" src="https://github.com/AileenDon/521_proj3/assets/120889846/0afd97c6-d942-4b2b-97b1-b4efad5bf811">
<img width="392" alt="Screenshot 2024-03-29 at 11 22 27 PM" src="https://github.com/AileenDon/521_proj3/assets/120889846/afdfa1b4-159e-4c8c-86df-8276ead9b9f1">

### Overflow Check:
- Function: check_overflow(result)
- Description: Checks if the result of the expression evaluation is within the specified bounds. If an overflow occurs, it adjusts the result accordingly.

<img width="398" alt="Screenshot 2024-03-29 at 11 13 24 PM" src="https://github.com/AileenDon/521_proj3/assets/120889846/f63f993c-355f-4908-86e3-78e16812d627">

### Evaluate and Check Overflow:
- Function: evaluate_expression(expression)
- Description: Evaluates a prefix expression and checks for overflow. Returns the final result or an overflow notification.
  
<img width="425" alt="Screenshot 2024-03-29 at 11 09 25 PM" src="https://github.com/AileenDon/521_proj3/assets/120889846/43c0fdf3-8670-486d-9299-397d667bf704">

### Extra Credits: Balanced Parentheses
- Function: check_parentheses_balance(expr)
- Description: Verifies that the parentheses in the expression are correctly balanced.
- Checks for balanced parentheses, outputting an error message for unbalanced expressions.

<img width="473" alt="Screenshot 2024-03-29 at 11 16 03 PM" src="https://github.com/AileenDon/521_proj3/assets/120889846/6897cead-c0f7-4d09-9359-45ac58003786">

## Usage
To use this tool, simply run the main() function. The user will be prompted to enter a mathematical expression. The tool then performs the following steps:

1. **Validates the input expression.**
2. **Checks for balanced parentheses.**
3. **Converts the expression from infix to prefix notation if valid.**
4. **Evaluates the prefix expression.**
5. **Checks for and handles any overflow in the evaluation result.**
6. **Displays the evaluation result or an error message if the input is invalid.**

