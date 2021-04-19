def validBraces(string):
    # add all opening braces to the stack
    # if closing parentheses detected compare it with peek element if its same kind with
    # peek element then pop else return false
    # if stack is empty return true
    brace_dict = {
                    "}": "{",
                    "]": "[",
                    ")": "("               
                 }
    brace_stack = []
    for i in range(len(string)):
        if string[i] in list(brace_dict.values()):
            brace_stack.append(string[i])
        if string[i] in list(brace_dict.keys()):
            if brace_stack and brace_stack[-1] == brace_dict[string[i]]:
                brace_stack.pop()
            else:
                return False
                
    if not brace_stack:
        return True
    return False