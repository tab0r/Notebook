import numpy as np

# activation functions
def sigmoid(x,deriv=False):
	if(deriv==True):
		e = sigmoid(x)
		return e*(1-e)
	return 1/(1+np.exp(-x))

def linear(x, deriv=False):
	pass

def pw_linear(x, a, b, deriv=False):
	pass

class Neuron(object):
	def __init__(self, n_inputs=1, weight_init="random", activation_function="sigmoid", learning_rate=0.1):
		self.inp = n_inputs
		self.s = activation_function
		if weight_init=="random":
			self.w = np.array([])
			for i in range(n_inputs+1):
				self.w[i] = np.random()
		# elif other weight init functions
		else:
			self.w = weight_init
		self.alpha=learning_rate

	def activate(self, input):
		in = np.array([1].extend(self.input))
		return self.s(np.dot(self.inp, self.w))

	def gradient_train(self, x, y):
		self.w += -alpha*

class NeuralNet(object):
	def __init__(self, n_neurons=2, n_inputs=2, n_outputs=2, activation_function="sigmoid"):
		self.n_neurons = 2
		self.n_inputs = n_inputs
		self.n_outputs = 2

	def activate(self, inputs):
		# input data to the net, return outputs
		pass

	def train(self, x, y):
		# adjust weights from a single


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

	# randomly initialize our weights with mean 0
	syn0 = 2*np.random.random((3,4)) - 1
	syn1 = 2*np.random.random((4,2)) - 1

	# learning rate and cycles
	alpha = 0.25
	cycles = 6000
	print("Training network with learning rate ", alpha)
	print("Cycles: ", cycles)

	for j in range(cycles):

		# Feed forward through layers 0, 1, and 2
	    l0 = X
	    l1 = nonlin(np.dot(l0,syn0))
	    l2 = nonlin(np.dot(l1,syn1))

	    # how much did we miss the target value?
	    l2_error = y - l2

	    if (j% 1000) == 0:
	        print("Error:" + str(np.mean(np.abs(l2_error))))

	    # in what direction is the target value?
	    # were we really sure? if so, don't change too much.
	    l2_delta = alpha*l2_error*nonlin(l2,deriv=True)

	    # how much did each l1 value contribute to the l2 error (according to the weights)?
	    l1_error = l2_delta.dot(syn1.T)

	    # in what direction is the target l1?
	    # were we really sure? if so, don't change too much.
	    l1_delta = alpha*l1_error * nonlin(l1,deriv=True)

	    syn1 += l1.T.dot(l2_delta)
	    syn0 += l0.T.dot(l1_delta)
