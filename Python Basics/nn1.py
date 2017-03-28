import numpy as np

def nonlin(x,deriv=False):
	if(deriv==True):
	    return x*(1-x)

	return 1/(1+np.exp(-x))
#change to list of ints
X = np.array([[0,0,0,0,0,0,0],
              [0,0,0,0,0,0,1],
              [0,0,0,0,0,1,0],
              [0,0,0,0,0,1,1],
              [0,0,0,0,1,0,0],
              [0,0,0,0,1,0,1],
              [0,0,0,0,1,1,0],
              [0,0,0,0,1,1,1],
              [0,0,0,1,0,0,0]
])
#list of binary form outputs
# use integer-valued geometric series to start for simplicity
y = np.array([[0,0,0,0,0,0,0],
              [0,0,0,0,0,0,1],
              [0,0,0,0,1,0,0],
              [0,0,0,1,0,0,1],
              [0,0,1,0,0,0,0],
              [0,0,1,1,0,0,1],
              [0,1,0,0,1,0,0],
              [0,1,1,0,0,0,1],
              [1,0,0,0,0,0,0]
])
#output neurons determine how far into the sequence we can go
#so for a geometric sequence a^n,
#want some k such that 2^k = a^n
#
np.random.seed(1)

# randomly initialize our weights with mean 0
syn0 = 2*np.random.random((7,4)) - 1
syn1 = 2*np.random.random((4,7)) - 1

for j in xrange(60000):

	# Feed forward through layers 0, 1, and 2
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    # how much did we miss the target value?
    l2_error = y - l2

    if (j% 10000) == 0:
        print "Error:" + str(np.mean(np.abs(l2_error)))

    # in what direction is the target value?
    # were we really sure? if so, don't change too much.
    l2_delta = l2_error*nonlin(l2,deriv=True)

    # how much did each l1 value contribute to the l2 error (according to the weights)?
    l1_error = l2_delta.dot(syn1.T)

    # in what direction is the target l1?
    # were we really sure? if so, don't change too much.
    l1_delta = l1_error * nonlin(l1,deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

#print training set current predictions

l0 = X
l1 = nonlin(np.dot(l0,syn0))
l2 = nonlin(np.dot(l1,syn1))

# how much did we miss the target value?
l2_error = y - l2

print(l2)
print(l2_error)

#test a few values
XT = np.array([
                [0,0,0,1,0,0,1]
#                [0,0,0,1,0,1,0],
#                [0,0,0,1,0,1,1]
])

YT = np.array([[1,0,1,0,0,0,1]
#               [1,1,0,0,1,0,0],
#               [1,1,1,1,0,0,1]
])

# Feed forward through layers 0, 1, and 2
l0 = XT
l1 = nonlin(np.dot(l0,syn0))
l2 = nonlin(np.dot(l1,syn1))

testError = YT-l2
print(l2)
print(YT)
#print(testError)
print "Test Set Error:" + str(np.mean(np.abs(testError)))
