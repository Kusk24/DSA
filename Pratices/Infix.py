def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def postfix_to_infix(postfix_expr):
    stack = []

    for token in postfix_expr:
        if is_number(token):
            stack.append(token)
        else:
            a = stack.pop()
            b = stack.pop()
            expression = f"({b} {token} {a})"
            stack.append(expression)

    return stack[0]


# Example usage
postfix_expr = input("Enter a postfix expression: ").split()
infix_expr = postfix_to_infix(postfix_expr)
print("Infix expression:", infix_expr)