def backspaceCompare(s, t):
    stack1 = []
    stack2 = []
    for i in range(len(s)):
        if s[i] == '#' and len(stack1) != 0:
            stack1.pop()
        elif s[i] == '#' and len(stack1) == 0:
            continue
        else:
            stack1.append(s[i])
    for j in range(len(t)):
        if t[j] == '#' and len(stack2) != 0:
            stack2.pop()
        elif t[j] == '#' and len(stack2) == 0:
            continue
        else:
            stack2.append(t[j])
    print(stack1, stack2)
    return stack1 == stack2

def main():
    #print(backspaceCompare("ab#c", "ad#c"))
    #print(backspaceCompare("ab##", "c#d#"))
    #print(backspaceCompare("a#c", "b"))
    print(backspaceCompare("y#fo##f", "y#f#o##f"))

main()