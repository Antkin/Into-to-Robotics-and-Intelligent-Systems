# Starter code for those trying to use LQR. Your
# K matrix controller should come from a call to lqr(A,B,Q,R),
# which we have provided. Below this are "dummy" matrices of the right
# type and size. If you fill in these with values you derive by hand
# they should work correctly to call the function.

# Here is the provided LQR function
import scipy.linalg
import numpy as np
def lqr( A, B, Q, R ):	
	x = scipy.linalg.solve_continuous_are( A, B, Q, R )
	k = np.linalg.inv(R) * np.dot( B.T, x )
	return k

# FOR YOU TODO: Fill in the values for A, B, Q and R here.
# Note that they should be matrices not scalars. 
# Then, figure out how to apply the resulting k
# to solve for a control, u, within the policyfn that balances the cartpole.

#First assign some variables
l = 0.5
m = 0.5
M = 0.5
b = 1
g = 9.82

A = np.array([[ 0, 1, 0, 0 ],
	          [ 0, (-4 * b)/(4*(M+m) - 3*m), 0, (3*m*g)/(4*(M+m) - 3*m) ],
	          [ 0, (-6 * b)/(l*(4*(M+m) - 3*m)), 0, (6*g*(M+m))/(l*(4*(M+m) - 3*m)) ],
              [ 0, 0, 1, 0 ]] )

B = np.array( [[0, 4/(4*(M+m) - 3*m), -1/(l*(4*(M+m) - 3*m)), 0 ]] )
B.shape = (4,1)

Q =  np.array([[ 1, 0, 0, 0 ],
       	       [ 0, 1, 0, 0 ],
	           [ 0, 0, 1, 0 ],
               [ 0, 0, 0, 10 ]] )

R = np.array([[1000]])
print( "A holds:",A)
print( "B holds:",B)
print( "Q holds:",Q)
print( "R holds:",R)

# Uncomment this to get the LQR gains k once you have
# filled in the correct matrices.
k = lqr( A, B, Q, R )
print( "k holds:",k)