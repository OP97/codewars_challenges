def solution(s):  # week 1
    splitted_list = []
    if len(s) % 2 != 0:
        s = s + "_"
    i = 0
    while i + 2 <= len(s):  # asd_
        splitted_list.append(s[i:i+2])
        i += 2
    return splitted_list

print(solution("Hello there"))  # splits input string into substrings of 2 chars
# ['He', 'll', 'o ', 'th', 'er', 'e_']