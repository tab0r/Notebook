import numpy as np
import pdb

def nonlin(x,deriv=False):
	if(deriv==True):
		e = nonlin(x)
		return e*(1-e)
		#return x*(1-x)
	return 1/(1+np.exp(-x))

def linear(x, deriv=False):
	pass

def pw_linear(x, a, b, deriv=False):
	pass

def relu():
	pass

def leaky_relu():
	pass

class NeuralNet(object):
	def __init__(self, stochastic=False):
		# randomly initialize our weights with mean 0
		self.syn0 = 2*np.random.random((3,4)) - 1
		self.syn1 = 2*np.random.random((4,2)) - 1
		self.stochastic = stochastic

	def fit(self, X, y, alpha, cycles, stochastic=False):
		print("Training network with learning rate ", alpha)
		print("Cycles: ", cycles)
		for j in range(cycles):
			# stochastic training loop
			# doesn't currently work
			if self.stochastic == True:
				for i,row in enumerate(X):
					#pdb.set_trace()
					l0 = np.array([row])
					l1 = np.array(nonlin(np.dot(l0,self.syn0)))
					#print("stochastic l1 shape:",l1.shape)
					l2 = np.array(nonlin(np.dot(l1,self.syn1)))
					#print("stochastic l2 shape:",l2.shape)
					#print(y[i,:], l2)
					l2_error = y[i,:] - l2
					#print(l2_error)
					self.update_syn(l0, l1, l2, y[i,:])
			else:
				# Feed forward through layers 0, 1, and 2
				l0 = X
				l1 = nonlin(np.dot(l0,self.syn0))
				l2 = nonlin(np.dot(l1,self.syn1))
				# how much did we miss the target value?
				l2_error = y - l2
				self.update_syn(l0, l1, l2, y)
			if (j% 1000) == 0:
				print("Error:" + str(np.mean(np.abs(l2_error))))

	def update_syn(self, l0, l1, l2, y):
		l2_error = y - l2
		# in what direction is the target value?
		# were we really sure? if so, don't change too much.
		l2_delta = alpha*l2_error*nonlin(l2,deriv=True)
		# how much did each l1 value contribute to the l2 error (according to the weights)?
		l1_error = l2_delta.dot(self.syn1.T)
		# in what direction is the target l1?
		# were we really sure? if so, don't change too much.
		#l1_delta = np.array([alpha*l1_error * nonlin(l1,deriv=True)])
		l1_delta = alpha*l1_error * nonlin(l1,deriv=True)
		#print("update syn l1 & l2_delta:",l1.shape, l2_delta.shape)
		syn1_delta = l1.T.dot(l2_delta)
		syn0_delta = l0.T.dot(l1_delta)
		self.syn1 += syn1_delta
		self.syn0 += syn0_delta

if __name__=="__main__":

	X = np.array([[0,0,1],
	            [0,1,1],
	            [1,0,1],
	            [1,1,1]])

	y = np.array([[0,1],
				[1,1],
				[1,0],
				[0,0]])

	np.random.seed(1)
	net = NeuralNet(stochastic=True)
	# learning rate and cycles
	alpha = 0.25
	cycles = 6000
	print("Neural network 'net' ready for training")
	#net.fit(X, y, alpha, cycles)
