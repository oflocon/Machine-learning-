def sigmoid(x):
	return 1/(1+numpy.exp(-x))

def costf(theta,x,y):
	lab_1=sigmoid(numpy.dot(x,theta)) #predict prob of label 1
	#numpy.dot(a,b) takes the dot product of 2 arrays here x and theta
	log_1=(-y)*numpy.log(lab_1)-(1-y)*numpy.log(1-lab_1)
	return log_.mean()

def c_grad(theta,x,y):
	lab_1=sigmoid(numpy.dot(x,theta))
	error=lab_1-y
	grad=numpy.dot(error,x_1)/y.size #gradient vector
	return grad
	
