#Name - Win Yu Maung
#ID - 6612054
#Sec - 542

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

Stack = []
postfix_expr = input().split()
for token in postfix_expr:
    if is_number(token):
        # Fill in code here for token being a number
        Stack.append(float(token))
    else:
        # Fill in code here for token not being a number
        a = Stack.pop(len(Stack)-1)
        b = Stack.pop(len(Stack)-1)

        if token == "+":
            Stack.append(b + a)
        elif token == "-":
            Stack.append(b - a)
        elif token == "*":
            Stack.append(b * a)
        elif token == "/":
            Stack.append(b / a)
        elif token == "%":
            Stack.append(b % a)
        elif token == "^":
            Stack.append(pow(b,a))
        
        
print('%.1f' % Stack[0])

    

        
