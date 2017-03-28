def queue_time(customers, n):
    # TODO
    if n == 1:
        k = 0
        for i in customers:
            k = k + int(i)
        return k
    elif len(customers) <= n:
        k = 0
        for i in customers:
            if i >= k: k = i
        return k
    else:
        tillSums = [0]*n
        #first batch of customers
        for i in range(0, n):
            tillSums[i] = tillSums[i] + customers[i]
            print(tillSums)
        #send customers to the lowest time
        for i in range(n, len(customers)):
            #low water mark test on tillSums
            m = tillSums[0]
            till = 0
            for l in range(1, n):
                if tillSums[l] <= m:
                    m = tillSums[l]
                    till = l
            tillSums[till] = tillSums[till] + customers[i]
        k = 0
        for i in range(0, n):
            if tillSums[i] >= k: k = tillSums[i]
        return k

print(queue_time([2, 17, 42, 13, 7, 1, 45, 45, 5, 47, 31, 44, 17, 32], 6))
