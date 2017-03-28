def presses(phrase):
    #your code here
    string = phrase.lower()

    alpha_split = [2] #should add to 26
    presses = 0
    for char in string:
        o = ord(char)
        #print(o)
        if o == 32 or o == 49:
            #space & one
            n = 1
        elif o == 48:
            #zero
            n = 2
        elif (o >49 and o < 55) or o == 56:
            #2-5, 7
            n = 4
        elif o == 55 or o == 57:
            n = 5
        elif o > 96 and o < 112:
            #first six keys
            n = (o-97)%3 + 1
        elif o > 111 and o < 116:
            #7
            n = (o-111)
        elif o > 115 and o < 119:
            #8
            n = (o-115)
            #9
        elif o > 118 and o < 123:
            n = (o-118)
        else:
            n = 1
        print(n)
        presses = presses + n

    return presses
print presses("how r u")
print presses("r")
