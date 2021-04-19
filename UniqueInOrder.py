def unique_in_order(iterable):  # week 1
    unique_list = []
    prev = None
    for item in iterable:
        if item != prev:
            unique_list.append(item)
            prev = item
    return unique_list

print(unique_in_order("AAAbbCCCdaaaEEEBBAAAA"))  # prints ['A', 'b', 'C', 'd', 'a', 'E', 'B', 'A']