import numpy as np
#python2
'''
anp = np.array([1,2,3])
print type(anp)
print anp.shape
print anp[0], anp[1], anp[2]
anp[0] = 5
print anp
#--------------------------------

print("SLICING")
ax = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
bx = ax[:2, 1:3]
print ax[0,1]
#bx[0,0] = 77
print ax[0,1]
print bx
#--------------------------------
print("array arange")
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print "a np.array:"
print a

b= np.array([0,2,0,1])
print "a np.arange 4:"
print a[np.arange(4), b]

a[np.arange(4), b] += 10
print "arange +10:"
print a

#------------------------------------
print("dtype")

x = np.array([1,2])
print x.dtype

x = np.array([1.0, 2.0])
print x.dtype

x = np.array([1,2], dtype=np.int64)
print x.dtype

#------------------------------------
print("float64")
xnp = np.array([[1,2], [3,4]], dtype = np.float64)
ynp = np.array([[5,6], [7,8]], dtype = np.float64)

print("add")
print xnp + ynp
print np.add(xnp, ynp)
print("sub")
print xnp-ynp
print np.subtract(xnp, ynp)

print("mul")
print xnp*ynp
print np.multiply(xnp, ynp)


#-------------------------------------
print("dot product")
xdot = np.array([[1,2], [3,4]])
ydot = np.array([[5,6], [7,8]])

#---------------------------------
print("array sum")

xsum = np.array([[1,2], [3,4]])
print np.sum(xsum)
print np.sum(xsum, axis = 0)
print np.sum(xsum, axis = 1)

#--------------------------------
print("transpose")
xT = np.array([[1,2], [3,4]])
print xT
print xT.T
'''

#---------------------------
from numpy.linalg import inv

c = np.array([[1,2,3],[4,5,6]])
cinv = inv(c)