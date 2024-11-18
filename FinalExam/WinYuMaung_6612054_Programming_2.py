#Name - Win Yu Maung,
# ID - 6612054,
# Section-542
Paren = list(input().split())

def CheckParanthesis(Paren):
    first = 0
    second = 0
    third = 0
    Latest = [0]
    for i in Paren:
        if i == "(":
            first += 1
            Latest.append(i)
        elif i == ")" and Latest[-1] == "(":
            first -= 1
            Latest.pop()
        elif i == "{":
            second += 1
            Latest.append(i)
        elif i == "}" and Latest[-1] == "{":
            second -= 1
            Latest.pop()
        elif i == "[":
            third += 1
            Latest.append(i)
        elif i == "]" and Latest[-1] == "[":
            third -= 1
            Latest.pop()

    if first == second == third == 0:
        print("Correct")
    else:
        print("Incorrect")

CheckParanthesis(Paren)