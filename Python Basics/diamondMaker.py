import math
from sys import argv

script, num = argv

def diamond(width):
    # build here
    #width = 2*n_floors-1
    if width % 2 == 0:
        return "Invalid: even"
    elif width < 0:
        return "Invalid: negative"
    else:
        height = width
        layers = ''
        for i in range(0, int((height-1)/2)):
            #print(i)
            j = 2*(i+1) - 1
            k = int(height/2) - i
            layers = layers + ' '*k+'*'*j+'\n'
        for l in range(int((height-1)/2), -1, -1):
            #print(l)
            j = 2*(l+1) - 1
            k = int(height/2) - l
            layers = layers + ' '*k+'*'*j+'\n'
        return layers

print(diamond(3))
print(diamond(int(num)))
