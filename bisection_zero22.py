from scipy.optimize import bisect
from numpy import sin,cos,exp

def f(x):
    return sin(cos(exp(x)))

b=bisect(f,-1,1)
print("zero of sin(cos(exp(x)))=0 is",b,".")

q=sin(cos(exp(b)))
print("value of function at found zero is",q,".")
