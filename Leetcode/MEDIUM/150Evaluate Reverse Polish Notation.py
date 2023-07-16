

def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i not in '+-*/':
            stack.append(int(i))
        elif i[0] == "-" and len(i) != 1:  # negative number
            stack.append(-int(i[1:]))
        else:
            num1, num2 = stack.pop(), stack.pop()
            if i == '+':
                stack.append(num2 + num1)  # right first, then left
            elif i == '-':
                stack.append(num2 - num1)
            elif i == '*':
                stack.append(num2 * num1)
            elif i == '/':
                stack.append(int(float(num2) / num1))
    return stack.pop()


def main():
    print(evalRPN(["2", "1", "+", "3", "*"]))

    print(evalRPN(["4", "13", "5", "/", "+"]))

    print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
    print(evalRPN(["4", "3", "-"]))

main()