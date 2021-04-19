def duplicate_count(text):  # week 1
    # inner loop to traverse through all text chars to compare with current char
    # outer loop to forward current char
    # if current char matches with char from inner loop add this to list
    # if it is already in the list continue
    repeated_chars = []
    for i in range(len(text)):
        for j in range(len(text)):
            if i != j:
                if text[i].lower() == text[j].lower() and text[j].lower() not in repeated_chars:
                    repeated_chars.append(text[i].lower())
            else:
                continue
    return len(repeated_chars)

print(duplicate_count("AAssddeeaaSS"))  # prints unique chars case insensitive