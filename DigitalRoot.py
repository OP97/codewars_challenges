def digital_root(n):
    # Given n, take the sum of the digits of n. 
    # If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
    # The input will be a non-negative integer.

    sum = 0
    str_n = str(n)
    for digit in str_n:
        sum += int(digit)
    if sum >= 10:
        return digital_root(sum)
    else:
        return sum