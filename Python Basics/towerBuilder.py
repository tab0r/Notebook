import math

def tower_builder(n_floors):
    # build here
    width = 2*n_floors-1
    floors = []
    for i in range(0, n_floors):
        #print(i)
        j = 2*(i+1) - 1
        k = n_floors - (i+1)
        floors.append(' '*k+'*'*j+' '*k)
    #floors.append('*'*width)
    return floors

print(tower_builder(3))
print(tower_builder(4))
print(tower_builder(2))
