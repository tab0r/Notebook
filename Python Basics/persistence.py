def persistence(n):
    digits = str(n)
    #return digits
    product = 1
    p_value = 0
    while len(str(digits)) > 1:
        for d in str(digits):
            product = product * int(d)
        p_value = p_value + 1
        digits = product
        product = 1
        print digits
    return p_value

print persistence(39)
