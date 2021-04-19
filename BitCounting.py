def count_bits(n):  # week 1
    bits = 0
    while n > 0:
        if n & 1:  # check if "n (and) 1" is true
            bits += 1
        n >>= 1  # Shift two bits right
    return bits

print(count_bits("1234"))  # 1234 is 10011010010 number of bits = 5