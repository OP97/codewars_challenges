def xo(s):  # week 1
    x_count = 0
    o_count = 0
      
    for c in s:
        if c.lower() == "x":
            x_count += 1
        elif c.lower() == "o":
            o_count += 1
        else:
            continue
            
    return x_count == o_count

print(xo("xxxssdsooo"))  # prints true if xs and os have same number of occurences else false