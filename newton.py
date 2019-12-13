from scipy.optimize import newton
from numpy import sin,cos,exp

def f(x):
    return sin(cos(exp(x)))

def g(x):
    return -exp(x)*sin(exp(x))*cos(cos(exp(x)))

p=newton(f,-1,fprime=lambda x:g(x))
print("zero of sin(cos(exp(x))) is",p,".")

q=newton(f,-0.1,fprime=lambda x:g(x))
print("zero of sin(cos(exp(x)))is",q,".")

