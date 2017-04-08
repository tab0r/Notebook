def answer(start, length):
    # this answer seems to provide correct solutions but times out
    if length == 1:
        return start
    else:
        ck_sum = start^(start+1)
        #print(ck_sum)
        rng = length**2
        # first block
        for i in range(2, length+1):
            ck_sum = ck_sum^(start+i)
            #print(ck_sum)
        for i in range(length+1, rng):
            if i % length <= length-1-(i//length):
                ck_sum = ck_sum^(start+i)
                #print(ck_sum)
    return ck_sum

def answer1(start, length):
    # this answer seems to provide correct solutions but times out
    ck_vals = [start]
    rng = start+length**2
    if length == 1:
        return start
    else:
        ck_vals.extend(
            [i for i in range(start+1, rng)
                if i % length <= length-1-(i//length)])
        return reduce(
            lambda x,y: x^y, ck_vals
                )

import operator as o

def answer2(start, length):
    # this answer seems to provide correct solutions but times out
    vals = []
    for i in range(0, length):
        print(vals)
        vals.append(start+length*i)
        vals.extend([start + length*i + x
            for x in range(1, length)
                if start + length*i + x % length < length-i])
    print(vals)
    return reduce(o.xor, vals)
