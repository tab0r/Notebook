a = set(["A", "B", "C","D"])
b = set(["E", "F", "G","H"])
s = set((a|b)|set(["I", "J"]))

c = set(s - (a|b))
d = set(s-a)&(s-b)
print c == d

e = set(s - (a&b))
f = set((s-a)|(s-b))
print e ==f

#def comb(n, k): return factorial(n)/factorial(k)*factorial(n-k)
from scipy.misc import comb
import math

lefthand_beers = ["Milk Stout", "Good Juju", "Fade to Black", "Polestar Pilsner"]
lefthand_beers += ["Black Jack Porter", "Wake Up Dead Imperial Stout","Warrior IPA"]

"""from itertools import combinations
n = len(lefthand_beers)
print comb(n, 4)

for c in combinations(lefthand_beers, 4)
    print c
"""
