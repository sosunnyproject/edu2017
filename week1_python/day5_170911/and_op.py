import numpy as np

x1 = np.array([0,0])
x2 = np.array([0,1])
x3 = np.array([1,0])
x4 = np.array([1,1])

w = np.array([1, 1])
b = 0

def and_op(w,x,b):
    s = sum(w*x)
    if s < 2:
        return 0
    else :
        return 1

and_op(w, x1, b)
and_op(w, x2, b)
and_op(w, x3, b)
and_op(w, x4, b)
print "w * x1 + b = ", and_op(w, x1, b)
print "w * x2 + b = ", and_op(w, x2, b)
print "w * x3 + b = ", and_op(w, x3, b)
print "w * x4 + b = ", and_op(w, x4, b)

#w*x1 + b =0