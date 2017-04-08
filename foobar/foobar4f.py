# this program only runs in Python 2!

import operator as o
import sys, timeit

#constructs a list of lists to chksum with xorList
def chunks(start, length):
    # whole chunks can be dropped out when their start is even and length = 2**k for some k
    # let's try making a list comprehension out of this
    return [(start+i*length, length-i)
        for i in xrange(0,length)
            if not ((start+i*length % 2 == 0)
                and (length-i & (length-i-1) == 0)
                and length-i > 1)]

def chunks1(start, length):
    chunks = []
    for i in xrange(0, length):
        s = start+i*length
        l = length - i
        chunks.append((s, l))
        #print chunks
    return chunks

#calculates reduce(o.xor, v) on v = (start, start+i, ... start+length)
def xorSeq((start, length)):
    if length > 1:
        # check for internal, droppable 0-sequences
        # if a 4-number sequence starts with an even number the whole sequence can be dropped
        vals = [0]
        while length > 4:
            oldStart = start
            if start % 2 == 0:
                start += 4*(length//4)
                length = (length + oldStart) - start
            else:
                vals.append(start)
                start += 1 + 4*(length//4)
                length = (length + oldStart) - start
        # if none just return the XOR of the whole thing
        vals.extend([x for x in xrange(start, start+length)])
        print(vals)
        return reduce(o.xor, vals)
    else:
        return start

def answer(start, length):
    vals = chunks(start, length)
    intermediate = map(xorSeq, vals)
    final = reduce(o.xor, intermediate)
    return final

# now we build a version that drops out zeroes at two levels, since x^0=x
def answer1(start, length):
    vals = chunks1(start, length)
    intermediate = map(xorSeq, vals)
    final = reduce(o.xor, intermediate)
    return final

n = int(sys.argv[1])
# start_time = timeit.default_timer()
# print("Chunking and chunk dropouts")
# print(answer(0,n))
# print(timeit.default_timer() - start_time)
#
# # not really slower at all, and sometimes faster
# start_time = timeit.default_timer()
# print("Chunking, no dropouts")
# print(answer1(0,n))
# print(timeit.default_timer() - start_time)

# about 5x slower
# start_time = timeit.default_timer()
# answer2(0,n)
# print("No chunking, no dropouts")
# print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
print("xorSeq from 0 & 1:")
print(xorSeq((0,n)))
print(xorSeq((1,n)))
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
print("reducing op.xor from 0 & 1:")
print(reduce(o.xor, xrange(0,n)))
print(reduce(o.xor, xrange(1,n)))
print(timeit.default_timer() - start_time)
