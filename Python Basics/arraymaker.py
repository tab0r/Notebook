for i in range(0, 255):
    #print("Input: " + str(i) + ", Output: " + str(pow(i, 2)))
    binNum = str(bin(pow(i, 1)))[2:]
    if len(binNum) < 8:
        for i in range(0, 8-len(binNum)):
            binNum = '0'+binNum
    commaNums = "["
    for char in binNum[0:-1]:
        commaNums = commaNums + char + ","
    commaNums = commaNums + binNum[len(binNum)-1]+"],"
    #print(binNum)
    print(commaNums)
