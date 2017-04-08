from multiprocessing import Pool
import operator as o
import sys

#constructs a list of lists to chksum with xorList
def chunks(start, length):
    # this answer seems to provide correct solutions but times out
    vals = []
    for i in range(0, length):
        #print(vals)
        vals.append((start+i*length, length-i))
    return vals

#calculates reduce(o.xor, v) on v = (start, start+i, ... start+length)
def xorList((start, length)):
    if length > 1:
        return reduce(o.xor, range(start, start+length))
    else:
        return start

def answer(start, length):
    vals = chunks(start, length)
    #print(vals)
    # this is the piece of code we can speed up with multiprocessing
    intermediate = map(xorList, vals)
    #print(intermediate)
    final = reduce(o.xor, intermediate)
    return final

def answerm(start, length):
    vals = chunks(start, length)
    # this is the piece of code we can speed up with multiprocessing
    # intermediate = map(xorList, vals)
    pool = Pool()
    intermediate = pool.map(xorList, vals)
    pool.close()
    pool.join()
    #print(intermediate)
    final = reduce(o.xor, intermediate)
    return final
