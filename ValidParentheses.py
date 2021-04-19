def valid_parentheses(string):  # week 1
    stack = []
    for i in range(len(string)):
        if string[i] == "(":
            stack.append(string[i])
        elif string[i] == ")" and stack and stack[-1] == "(":
            stack.pop()
        else:
            if string[i] == "(" or string[i] == ")":
                stack.append(string[i])
            continue
    return not stack

print(valid_parentheses("bnfrkkqpmj(gypelr)xkjk)(v"))  # returns true if parentheses matches correctly