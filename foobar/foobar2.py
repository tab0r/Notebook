import itertools, sys, timeit
import numpy.random as npr

def listtoNum(l):
    return sum([int(x)*10**i for i, x in enumerate(l)])

def answer(l, n=None):
    # this one worked!
    if n == None:
        n = len(l) - 1
    val = 0
    if n > 0:
        #print(intList)
        for j in range(n):
            intList = sorted(map(int, l), reverse = True)
            l0 = intList.pop(j)*(10**n)
            print(l0)
            val = 0
            vals = [x + l0 for x in
                [listtoNum(p) for p in itertools.permutations(intList, n)]
                        if (x % 3 + l0 % 3) % 3 == 0]
            print(vals)
            vals.append(0)
            val += max(vals)
            if val > 0:
                return val
            else:
                return answer(l, n-1)
    elif n == 0 and int(l[0])%3 == 0:
        return l[0]

    return val

def answer2(l, n=None):
    # your code here
    if n == None:
        n = len(l) - 1
    val = 0
    if n > 0:
        #print(intList)
        intList = sorted(map(int, l), reverse = True)
        for j in range(len(l)-1):
            l0 = intList.pop(j)*(10**n)
            #rint(l0)
            val = 0
            vals = [x + l0 for x in
                [listtoNum(p) for p in itertools.permutations(intList, n)]
                        if x % 3 == l0 % 3]
                #print(vals)
            vals.append(0)
            val += max(vals)
            if val > 0:
                return val
            else:
                return answer(l, n-1)
    elif n == 0 and int(l[0])%3 == 0:
        return l[0]

    return val

def answer1(l):
    # your code here
    #l.sort(reverse = True)
    val = 0
    if len(l) > 1:
        for i in range(len(l), 1, -1):
            vals = [x for x in
                    map(listtoNum, itertools.permutations(l, i))
                        if x % 3 == 0]
            vals.append(0)
            val += max(vals)
            if val > 0: return val
    elif len(l) == 1 and int(l[0])%3 == 0:
        return l[0]
    else:
        return 0
                        #for i in range(len(l), 1, -1)])
    return val


import time

def stressTest(n=None, s=None, l=None):
    if n==None:
        m=10
    else:
        m=n

    if s==None:
        s=1
    npr.seed(s)
    if l==None:
        inputList = list(npr.randint(10, size = m))
    else:
        inputList = l
    print(inputList)
    start = time.time()
    answerVal = answer(inputList)
    end = time.time()
    print(end - start)
    start = time.time()
    answer1Val = answer1(inputList)
    end = time.time()
    print(end - start)
    print("Answer: " + str(answerVal))
    print("Answer1: " + str(answer1Val))


if __name__ == '__main__':
    print(answer(['3', '4', '5']))
    print(answer1(['3', '4', '5']))
    if sys.argv[1]:
        vals = list(sys.argv[1:])
        print(answer(vals))
        print(answer1(vals))
        stressTest(l=vals)
