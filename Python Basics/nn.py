import numpy as np

def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))

XData = np.array([
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,1],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,1,1],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,0,1,0,1],
	[0,0,0,0,0,1,1,0],
	[0,0,0,0,0,1,1,1],
	[0,0,0,0,1,0,0,0],
	[0,0,0,0,1,0,0,1],
	[0,0,0,0,1,0,1,0],
	[0,0,0,0,1,0,1,1],
	[0,0,0,0,1,1,0,0],
	[0,0,0,0,1,1,0,1],
	[0,0,0,0,1,1,1,0],
	[0,0,0,0,1,1,1,1],
	[0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,0,1],
	[0,0,0,1,0,0,1,0],
	[0,0,0,1,0,0,1,1],
	[0,0,0,1,0,1,0,0],
	[0,0,0,1,0,1,0,1],
	[0,0,0,1,0,1,1,0],
	[0,0,0,1,0,1,1,1],
	[0,0,0,1,1,0,0,0],
	[0,0,0,1,1,0,0,1],
	[0,0,0,1,1,0,1,0],
	[0,0,0,1,1,0,1,1],
	[0,0,0,1,1,1,0,0],
	[0,0,0,1,1,1,0,1],
	[0,0,0,1,1,1,1,0],
	[0,0,0,1,1,1,1,1],
	[0,0,1,0,0,0,0,0],
	[0,0,1,0,0,0,0,1],
	[0,0,1,0,0,0,1,0],
	[0,0,1,0,0,0,1,1],
	[0,0,1,0,0,1,0,0],
	[0,0,1,0,0,1,0,1],
	[0,0,1,0,0,1,1,0],
	[0,0,1,0,0,1,1,1],
	[0,0,1,0,1,0,0,0],
	[0,0,1,0,1,0,0,1],
	[0,0,1,0,1,0,1,0],
	[0,0,1,0,1,0,1,1],
	[0,0,1,0,1,1,0,0],
	[0,0,1,0,1,1,0,1],
	[0,0,1,0,1,1,1,0],
	[0,0,1,0,1,1,1,1],
	[0,0,1,1,0,0,0,0],
	[0,0,1,1,0,0,0,1],
	[0,0,1,1,0,0,1,0],
	[0,0,1,1,0,0,1,1],
	[0,0,1,1,0,1,0,0],
	[0,0,1,1,0,1,0,1],
	[0,0,1,1,0,1,1,0],
	[0,0,1,1,0,1,1,1],
	[0,0,1,1,1,0,0,0],
	[0,0,1,1,1,0,0,1],
	[0,0,1,1,1,0,1,0],
	[0,0,1,1,1,0,1,1],
	[0,0,1,1,1,1,0,0],
	[0,0,1,1,1,1,0,1],
	[0,0,1,1,1,1,1,0],
	[0,0,1,1,1,1,1,1],
	[0,1,0,0,0,0,0,0],
	[0,1,0,0,0,0,0,1],
	[0,1,0,0,0,0,1,0],
	[0,1,0,0,0,0,1,1],
	[0,1,0,0,0,1,0,0],
	[0,1,0,0,0,1,0,1],
	[0,1,0,0,0,1,1,0],
	[0,1,0,0,0,1,1,1],
	[0,1,0,0,1,0,0,0],
	[0,1,0,0,1,0,0,1],
	[0,1,0,0,1,0,1,0],
	[0,1,0,0,1,0,1,1],
	[0,1,0,0,1,1,0,0],
	[0,1,0,0,1,1,0,1],
	[0,1,0,0,1,1,1,0],
	[0,1,0,0,1,1,1,1],
	[0,1,0,1,0,0,0,0],
	[0,1,0,1,0,0,0,1],
	[0,1,0,1,0,0,1,0],
	[0,1,0,1,0,0,1,1],
	[0,1,0,1,0,1,0,0],
	[0,1,0,1,0,1,0,1],
	[0,1,0,1,0,1,1,0],
	[0,1,0,1,0,1,1,1],
	[0,1,0,1,1,0,0,0],
	[0,1,0,1,1,0,0,1],
	[0,1,0,1,1,0,1,0],
	[0,1,0,1,1,0,1,1],
	[0,1,0,1,1,1,0,0],
	[0,1,0,1,1,1,0,1],
	[0,1,0,1,1,1,1,0],
	[0,1,0,1,1,1,1,1],
	[0,1,1,0,0,0,0,0],
	[0,1,1,0,0,0,0,1],
	[0,1,1,0,0,0,1,0],
	[0,1,1,0,0,0,1,1],
	[0,1,1,0,0,1,0,0],
	[0,1,1,0,0,1,0,1],
	[0,1,1,0,0,1,1,0],
	[0,1,1,0,0,1,1,1],
	[0,1,1,0,1,0,0,0],
	[0,1,1,0,1,0,0,1],
	[0,1,1,0,1,0,1,0],
	[0,1,1,0,1,0,1,1],
	[0,1,1,0,1,1,0,0],
	[0,1,1,0,1,1,0,1],
	[0,1,1,0,1,1,1,0],
	[0,1,1,0,1,1,1,1],
	[0,1,1,1,0,0,0,0],
	[0,1,1,1,0,0,0,1],
	[0,1,1,1,0,0,1,0],
	[0,1,1,1,0,0,1,1],
	[0,1,1,1,0,1,0,0],
	[0,1,1,1,0,1,0,1],
	[0,1,1,1,0,1,1,0],
	[0,1,1,1,0,1,1,1],
	[0,1,1,1,1,0,0,0],
	[0,1,1,1,1,0,0,1],
	[0,1,1,1,1,0,1,0],
	[0,1,1,1,1,0,1,1],
	[0,1,1,1,1,1,0,0],
	[0,1,1,1,1,1,0,1],
	[0,1,1,1,1,1,1,0],
	[0,1,1,1,1,1,1,1],
	[1,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,1,0],
	[1,0,0,0,0,0,1,1],
	[1,0,0,0,0,1,0,0],
	[1,0,0,0,0,1,0,1],
	[1,0,0,0,0,1,1,0],
	[1,0,0,0,0,1,1,1],
	[1,0,0,0,1,0,0,0],
	[1,0,0,0,1,0,0,1],
	[1,0,0,0,1,0,1,0],
	[1,0,0,0,1,0,1,1],
	[1,0,0,0,1,1,0,0],
	[1,0,0,0,1,1,0,1],
	[1,0,0,0,1,1,1,0],
	[1,0,0,0,1,1,1,1],
	[1,0,0,1,0,0,0,0],
	[1,0,0,1,0,0,0,1],
	[1,0,0,1,0,0,1,0],
	[1,0,0,1,0,0,1,1],
	[1,0,0,1,0,1,0,0],
	[1,0,0,1,0,1,0,1],
	[1,0,0,1,0,1,1,0],
	[1,0,0,1,0,1,1,1],
	[1,0,0,1,1,0,0,0],
	[1,0,0,1,1,0,0,1],
	[1,0,0,1,1,0,1,0],
	[1,0,0,1,1,0,1,1],
	[1,0,0,1,1,1,0,0],
	[1,0,0,1,1,1,0,1],
	[1,0,0,1,1,1,1,0],
	[1,0,0,1,1,1,1,1],
	[1,0,1,0,0,0,0,0],
	[1,0,1,0,0,0,0,1],
	[1,0,1,0,0,0,1,0],
	[1,0,1,0,0,0,1,1],
	[1,0,1,0,0,1,0,0],
	[1,0,1,0,0,1,0,1],
	[1,0,1,0,0,1,1,0],
	[1,0,1,0,0,1,1,1],
	[1,0,1,0,1,0,0,0],
	[1,0,1,0,1,0,0,1],
	[1,0,1,0,1,0,1,0],
	[1,0,1,0,1,0,1,1],
	[1,0,1,0,1,1,0,0],
	[1,0,1,0,1,1,0,1],
	[1,0,1,0,1,1,1,0],
	[1,0,1,0,1,1,1,1],
	[1,0,1,1,0,0,0,0],
	[1,0,1,1,0,0,0,1],
	[1,0,1,1,0,0,1,0],
	[1,0,1,1,0,0,1,1],
	[1,0,1,1,0,1,0,0],
	[1,0,1,1,0,1,0,1],
	[1,0,1,1,0,1,1,0],
	[1,0,1,1,0,1,1,1],
	[1,0,1,1,1,0,0,0],
	[1,0,1,1,1,0,0,1],
	[1,0,1,1,1,0,1,0],
	[1,0,1,1,1,0,1,1],
	[1,0,1,1,1,1,0,0],
	[1,0,1,1,1,1,0,1],
	[1,0,1,1,1,1,1,0],
	[1,0,1,1,1,1,1,1],
	[1,1,0,0,0,0,0,0],
	[1,1,0,0,0,0,0,1],
	[1,1,0,0,0,0,1,0],
	[1,1,0,0,0,0,1,1],
	[1,1,0,0,0,1,0,0],
	[1,1,0,0,0,1,0,1],
	[1,1,0,0,0,1,1,0],
	[1,1,0,0,0,1,1,1],
	[1,1,0,0,1,0,0,0],
	[1,1,0,0,1,0,0,1],
	[1,1,0,0,1,0,1,0],
	[1,1,0,0,1,0,1,1],
	[1,1,0,0,1,1,0,0],
	[1,1,0,0,1,1,0,1],
	[1,1,0,0,1,1,1,0],
	[1,1,0,0,1,1,1,1],
	[1,1,0,1,0,0,0,0],
	[1,1,0,1,0,0,0,1],
	[1,1,0,1,0,0,1,0],
	[1,1,0,1,0,0,1,1],
	[1,1,0,1,0,1,0,0],
	[1,1,0,1,0,1,0,1],
	[1,1,0,1,0,1,1,0],
	[1,1,0,1,0,1,1,1],
	[1,1,0,1,1,0,0,0],
	[1,1,0,1,1,0,0,1],
	[1,1,0,1,1,0,1,0],
	[1,1,0,1,1,0,1,1],
	[1,1,0,1,1,1,0,0],
	[1,1,0,1,1,1,0,1],
	[1,1,0,1,1,1,1,0],
	[1,1,0,1,1,1,1,1],
	[1,1,1,0,0,0,0,0],
	[1,1,1,0,0,0,0,1],
	[1,1,1,0,0,0,1,0],
	[1,1,1,0,0,0,1,1],
	[1,1,1,0,0,1,0,0],
	[1,1,1,0,0,1,0,1],
	[1,1,1,0,0,1,1,0],
	[1,1,1,0,0,1,1,1],
	[1,1,1,0,1,0,0,0],
	[1,1,1,0,1,0,0,1],
	[1,1,1,0,1,0,1,0],
	[1,1,1,0,1,0,1,1],
	[1,1,1,0,1,1,0,0],
	[1,1,1,0,1,1,0,1],
	[1,1,1,0,1,1,1,0],
	[1,1,1,0,1,1,1,1],
	[1,1,1,1,0,0,0,0],
	[1,1,1,1,0,0,0,1],
	[1,1,1,1,0,0,1,0],
	[1,1,1,1,0,0,1,1],
	[1,1,1,1,0,1,0,0],
	[1,1,1,1,0,1,0,1],
	[1,1,1,1,0,1,1,0],
	[1,1,1,1,0,1,1,1],
	[1,1,1,1,1,0,0,0],
	[1,1,1,1,1,0,0,1],
	[1,1,1,1,1,0,1,0],
	[1,1,1,1,1,0,1,1],
	[1,1,1,1,1,1,0,0],
	[1,1,1,1,1,1,0,1],
	[1,1,1,1,1,1,1,0]
])

yData = np.array([
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
	[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1],
	[0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0],
	[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1],
	[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1],
	[0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0],
	[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1],
	[0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0],
	[0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1],
	[0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0],
	[0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1],
	[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1],
	[0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0],
	[0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,1],
	[0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],
	[0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,1],
	[0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0],
	[0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1],
	[0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0],
	[0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,1],
	[0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0],
	[0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1],
	[0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0],
	[0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,1],
	[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0],
	[0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1],
	[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1],
	[0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0],
	[0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,1],
	[0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0],
	[0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,1],
	[0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,0],
	[0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1],
	[0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],
	[0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1],
	[0,0,0,0,0,1,1,0,1,1,1,0,0,1,0,0],
	[0,0,0,0,0,1,1,1,0,0,1,1,1,0,0,1],
	[0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0],
	[0,0,0,0,0,1,1,1,1,1,1,0,1,0,0,1],
	[0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0],
	[0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,1],
	[0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],
	[0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,1],
	[0,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0],
	[0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1],
	[0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,1,0,1,1,1,1,1,0,0,1],
	[0,0,0,0,1,0,1,1,0,1,1,0,0,1,0,0],
	[0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1],
	[0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0],
	[0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1],
	[0,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0],
	[0,0,0,0,1,1,0,1,1,0,0,1,1,0,0,1],
	[0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0],
	[0,0,0,0,1,1,1,0,1,0,0,0,1,0,0,1],
	[0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0],
	[0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,1],
	[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
	[0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0],
	[0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1],
	[0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0],
	[0,0,0,1,0,0,1,0,1,0,0,1,1,0,0,1],
	[0,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0],
	[0,0,0,1,0,0,1,1,1,0,1,1,0,0,0,1],
	[0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0],
	[0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,1],
	[0,0,0,1,0,1,0,1,0,1,1,0,0,1,0,0],
	[0,0,0,1,0,1,0,1,1,1,1,1,1,0,0,1],
	[0,0,0,1,0,1,1,0,1,0,0,1,0,0,0,0],
	[0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1],
	[0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0],
	[0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1],
	[0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0],
	[0,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1],
	[0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,0],
	[0,0,0,1,1,0,1,0,1,1,1,0,1,0,0,1],
	[0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0],
	[0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1],
	[0,0,0,1,1,1,0,0,1,1,1,0,0,1,0,0],
	[0,0,0,1,1,1,0,1,1,0,0,1,0,0,0,1],
	[0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0],
	[0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,1],
	[0,0,0,1,1,1,1,1,1,0,1,0,0,1,0,0],
	[0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1],
	[0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0],
	[0,0,1,0,0,0,0,1,1,1,0,0,1,0,0,1],
	[0,0,1,0,0,0,1,0,1,0,0,0,0,1,0,0],
	[0,0,1,0,0,0,1,1,0,1,0,0,0,0,0,1],
	[0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,1],
	[0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0],
	[0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1],
	[0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0],
	[0,0,1,0,0,1,1,1,1,1,0,1,1,0,0,1],
	[0,0,1,0,1,0,0,0,1,0,1,0,0,1,0,0],
	[0,0,1,0,1,0,0,1,0,1,1,1,0,0,0,1],
	[0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0],
	[0,0,1,0,1,0,1,1,0,0,0,1,0,0,0,1],
	[0,0,1,0,1,0,1,1,1,1,1,0,0,1,0,0],
	[0,0,1,0,1,1,0,0,1,0,1,1,1,0,0,1],
	[0,0,1,0,1,1,0,1,1,0,0,1,0,0,0,0],
	[0,0,1,0,1,1,1,0,0,1,1,0,1,0,0,1],
	[0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0],
	[0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1],
	[0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0],
	[0,0,1,1,0,0,0,1,1,1,1,0,0,0,0,1],
	[0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0],
	[0,0,1,1,0,0,1,1,1,0,1,0,1,0,0,1],
	[0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0],
	[0,0,1,1,0,1,0,1,0,1,1,1,1,0,0,1],
	[0,0,1,1,0,1,1,0,0,1,1,0,0,1,0,0],
	[0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,1],
	[0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0],
	[0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,1],
	[0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0],
	[0,0,1,1,1,0,1,1,0,0,0,1,1,0,0,1],
	[0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0],
	[0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1],
	[0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0],
	[0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
	[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
	[0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0],
	[0,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1],
	[0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
	[0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,1],
	[0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0],
	[0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,1],
	[0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
	[0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1],
	[0,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0],
	[0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,1],
	[0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,0],
	[0,1,0,0,1,1,0,1,1,0,1,0,1,0,0,1],
	[0,1,0,0,1,1,1,0,1,1,0,0,0,1,0,0],
	[0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1],
	[0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0],
	[0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1],
	[0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,0],
	[0,1,0,1,0,1,0,0,0,1,1,0,1,0,0,1],
	[0,1,0,1,0,1,0,1,1,0,0,1,0,0,0,0],
	[0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,1],
	[0,1,0,1,0,1,1,1,1,1,1,0,0,1,0,0],
	[0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,1],
	[0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0],
	[0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,1],
	[0,1,0,1,1,1,0,0,1,0,1,0,0,1,0,0],
	[0,1,0,1,1,1,0,1,1,1,0,1,1,0,0,1],
	[0,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0],
	[0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,1],
	[0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0],
	[0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,1],
	[0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,0,0,1,0,1,0,1,0,0,0,0,0,1],
	[0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,0],
	[0,1,1,0,0,1,1,1,1,1,0,0,1,0,0,1],
	[0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,0],
	[0,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1],
	[0,1,1,0,1,0,1,1,1,0,1,0,0,1,0,0],
	[0,1,1,0,1,1,0,0,1,1,1,1,0,0,0,1],
	[0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0],
	[0,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1],
	[0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,0],
	[0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,1],
	[0,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0],
	[0,1,1,1,0,1,0,0,1,1,1,0,1,0,0,1],
	[0,1,1,1,0,1,1,0,0,1,0,0,0,1,0,0],
	[0,1,1,1,0,1,1,1,1,0,1,0,0,0,0,1],
	[0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,0,1,0,0,1,1,0,0,0,0,1],
	[0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,0],
	[0,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1],
	[0,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1],
	[1,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0],
	[1,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1],
	[1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0],
	[1,0,0,0,0,1,0,1,1,0,1,1,0,0,0,1],
	[1,0,0,0,0,1,1,1,0,0,1,0,0,1,0,0],
	[1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1],
	[1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
	[1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1],
	[1,0,0,0,1,1,0,1,0,0,0,0,0,1,0,0],
	[1,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1],
	[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
	[1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1],
	[1,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0],
	[1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1],
	[1,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0],
	[1,0,0,1,0,1,1,1,1,0,0,1,1,0,0,1],
	[1,0,0,1,1,0,0,1,0,0,1,0,0,1,0,0],
	[1,0,0,1,1,0,1,0,1,0,1,1,0,0,0,1],
	[1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0],
	[1,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1],
	[1,0,0,1,1,1,1,1,0,1,1,0,0,1,0,0],
	[1,0,1,0,0,0,0,0,1,1,1,1,1,0,0,1],
	[1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0],
	[1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1],
	[1,0,1,0,0,1,0,1,1,1,0,0,0,1,0,0],
	[1,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1],
	[1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0],
	[1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1],
	[1,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0],
	[1,0,1,0,1,1,0,1,1,1,1,0,1,0,0,1],
	[1,0,1,0,1,1,1,1,1,0,0,1,0,0,0,0],
	[1,0,1,1,0,0,0,1,0,0,1,1,1,0,0,1],
	[1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0],
	[1,0,1,1,0,1,0,0,1,0,0,1,0,0,0,1],
	[1,0,1,1,0,1,1,0,0,1,0,0,0,0,0,0],
	[1,0,1,1,0,1,1,1,1,1,1,1,0,0,0,1],
	[1,0,1,1,1,0,0,1,1,0,1,0,0,1,0,0],
	[1,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1],
	[1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0],
	[1,0,1,1,1,1,1,0,1,1,0,0,1,0,0,1],
	[1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0],
	[1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1],
	[1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
	[1,1,0,0,0,1,0,1,1,1,0,0,0,0,0,1],
	[1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,0],
	[1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1],
	[1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0],
	[1,1,0,0,1,1,0,0,1,1,0,1,1,0,0,1],
	[1,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0],
	[1,1,0,1,0,0,0,0,0,1,1,1,0,0,0,1],
	[1,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0],
	[1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1],
	[1,1,0,1,0,1,0,1,1,1,1,0,0,1,0,0],
	[1,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1],
	[1,1,0,1,1,0,0,1,1,0,0,1,0,0,0,0],
	[1,1,0,1,1,0,1,1,0,1,1,0,1,0,0,1],
	[1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,0],
	[1,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1],
	[1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0],
	[1,1,1,0,0,0,1,0,1,1,1,0,0,0,0,1],
	[1,1,1,0,0,1,0,0,1,1,0,0,0,1,0,0],
	[1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,1],
	[1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0],
	[1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,1],
	[1,1,1,0,1,1,0,0,0,1,1,0,0,1,0,0],
	[1,1,1,0,1,1,1,0,0,1,0,1,0,0,0,1],
	[1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
	[1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,1],
	[1,1,1,1,0,1,0,0,0,0,1,0,0,1,0,0],
	[1,1,1,1,0,1,1,0,0,0,0,1,1,0,0,1],
	[1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0],
	[1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1],
	[1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0]
])
#for t in range(1, 254):
t = 255
y = XData
X = yData

#number of hidden layer neurons
n1 = 19
n2 = 9
#for n in range(2,7):
np.random.seed(1)

# randomly initialize our weights with mean 0
# note: this network was provided with random weights from -1 to 1,
# we're going to paramaterize it so I can experiment with "weak weights"
w = 1
syn0 = 2*w*np.random.random((16,n1)) - w
syn1 = 2*w*np.random.random((n1,n2)) - w
syn2 = 2*w*np.random.random((n2,8)) - w

for j in xrange(6000):
	# Feed forward through layers 0, 1, and 2
	l0 = X
	l1 = nonlin(np.dot(l0,syn0))
	l2 = nonlin(np.dot(l1,syn1))
	l3 = nonlin(np.dot(l2,syn2))

	# how much did we miss the target value?
	l3_error = y - l3
	l3_delta = l3_error*nonlin(l3,deriv=True)
	l2_error = l3_delta.dot(syn2.T)

	if (j% 10000) == 0: print "Error:" + str(np.mean(np.abs(l3_error)))

	# in what direction is the target value?
	# were we really sure? if so, don't change too much.
	l2_delta = l2_error*nonlin(l2,deriv=True)

	# how much did each l1 value contribute to the l2 error (according to the weights)?
	l1_error = l2_delta.dot(syn1.T)

	# in what direction is the target l1?
	# were we really sure? if so, don't change too much.
	l1_delta = l1_error * nonlin(l1,deriv=True)

	syn2 += l2.T.dot(l3_delta)
	syn1 += l1.T.dot(l2_delta)
	syn0 += l0.T.dot(l1_delta)
"""
	#test the sequence value immediately after training set
		XT = XData[t+1, :]

		YT = yData[t+1, :]
"""
# Feed forward through layers 0, 1, and 2
l0 = X
l1 = nonlin(np.dot(l0,syn0))
l2 = nonlin(np.dot(l1,syn1))
l3 = nonlin(np.dot(l2,syn2))
#testError = y-l3
print l3.shape
y2 = []
for i in range(0, 255):
	l3bin = ""
	y2.append(i*i)
	for b in l3[i,:]:
		#print("%.0f" % b),
		if b >= 0.5:
			l3bin += str(1)
		else:
			l3bin += str(0)
	print(str(int(l3bin, 2)))

weirdNum = sum(y2)/255
print weirdNum
#print(YT)
#print(testError)
#print str(t+1) + "," + str(np.mean(np.abs(testError)))
#print str(np.mean(np.abs(testError)))