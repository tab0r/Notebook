# this program only runs in Python 2!

import operator as o
import sys, timeit

#constructs a list of lists to chksum with xorList
def chunks(start, length):
    # whole chunks can be dropped out when their start is even and length = 2**k for some k
    # let's try making a list comprehension out of this
    return [(start+i*length, length-i)
        for i in range(0,length)
            if not ((start+i*length % 2 == 0)
                and (length-i & (length-i-1) == 0)
                and length-i > 1)]

#calculates reduce(o.xor, v) on v = (start, start+i, ... start+length)
def xorList((start, length)):
    if length > 1:
        return reduce(o.xor, range(start, start+length))
    else:
        return start

def answer(start, length):
    vals = chunks(start, length)
    intermediate = map(xorList, vals)
    final = reduce(o.xor, intermediate)
    return final

n = int(sys.argv[1])
start_time = timeit.default_timer()
print answer(0,n)
print(timeit.default_timer() - start_time)
