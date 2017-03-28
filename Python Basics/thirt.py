def thirt(n):
    # your code
    remainders = [1, 10, 9, 12, 3, 4]
    digits = list(str(n))
    digitset = list(str(n))
    k = int(n)
    r = 0
    while 1:
        r = 0
        for i in range(0,len(digits)):
            r = r + int(digits[len(digits)-i-1])*remainders[i%6]
            #print(r)
        if list(str(r)) == digits: break
        digits.clear()
        digits = list(str(r))
        digitset = set(list(str(r)))
        #print(r)
    return r

print(thirt(1234567))
