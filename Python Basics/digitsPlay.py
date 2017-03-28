from sys import argv
import math

def dig_pow(n, p):
    # your code
    digits = list(str(n))
    a = len(digits)
    powerSum = 0
    for i in range(p, p+a): #len(list(n))):
        powerSum = powerSum + int(digits[i-p])**(i)
        #print(powerSum)
    if powerSum/n == math.floor(powerSum/n):
        k = powerSum/n
    else:
        k = -1
    return k

print(dig_pow(89, 1))
print(dig_pow(695, 2))
print(dig_pow(46288, 3))
