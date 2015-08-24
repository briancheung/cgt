# This file was autogenerated by gen_py.py. Do not edit.
from . import core

def abs(x):
    "Applies function abs elementwise to argument x"
    return core.Result(core.ElwiseUnary("abs"), [x])
    
def ceil(x):
    "Applies function ceil elementwise to argument x"
    return core.Result(core.ElwiseUnary("ceil"), [x])
    
def conj(x):
    "Applies function conj elementwise to argument x"
    return core.Result(core.ElwiseUnary("conj"), [x])
    
def cos(x):
    "Applies function cos elementwise to argument x"
    return core.Result(core.ElwiseUnary("cos"), [x])
    
def exp(x):
    "Applies function exp elementwise to argument x"
    return core.Result(core.ElwiseUnary("exp"), [x])
    
def iceil(x):
    "Applies function iceil elementwise to argument x"
    return core.Result(core.ElwiseUnary("iceil"), [x])
    
def ifloor(x):
    "Applies function ifloor elementwise to argument x"
    return core.Result(core.ElwiseUnary("ifloor"), [x])
    
def log(x):
    "Applies function log elementwise to argument x"
    return core.Result(core.ElwiseUnary("log"), [x])
    
def negative(x):
    "Applies function negative elementwise to argument x"
    return core.Result(core.ElwiseUnary("neg"), [x])
    
def sigmoid(x):
    "Applies function sigmoid elementwise to argument x"
    return core.Result(core.ElwiseUnary("sigmoid"), [x])
    
def sign(x):
    "Applies function sign elementwise to argument x"
    return core.Result(core.ElwiseUnary("sign"), [x])
    
def sin(x):
    "Applies function sin elementwise to argument x"
    return core.Result(core.ElwiseUnary("sin"), [x])
    
def sqrt(x):
    "Applies function sqrt elementwise to argument x"
    return core.Result(core.ElwiseUnary("sqrt"), [x])
    
def square(x):
    "Applies function square elementwise to argument x"
    return core.Result(core.ElwiseUnary("square"), [x])
    
def tanh(x):
    "Applies function tanh elementwise to argument x"
    return core.Result(core.ElwiseUnary("tanh"), [x])
    
def add(x, y):
    "Applies function add elementwise to arguments x,y"
    return core.elwise_binary("+", x,y)
    
def divide(x, y):
    "Applies function divide elementwise to arguments x,y"
    return core.elwise_binary("/", x,y)
    
def equal(x, y):
    "Applies function equal elementwise to arguments x,y"
    return core.elwise_binary("==", x,y)
    
def greater(x, y):
    "Applies function greater elementwise to arguments x,y"
    return core.elwise_binary(">", x,y)
    
def greater_equal(x, y):
    "Applies function greater_equal elementwise to arguments x,y"
    return core.elwise_binary(">=", x,y)
    
def less(x, y):
    "Applies function less elementwise to arguments x,y"
    return core.elwise_binary("<", x,y)
    
def less_equal(x, y):
    "Applies function less_equal elementwise to arguments x,y"
    return core.elwise_binary("<=", x,y)
    
def multiply(x, y):
    "Applies function multiply elementwise to arguments x,y"
    return core.elwise_binary("*", x,y)
    
def not_equal(x, y):
    "Applies function not_equal elementwise to arguments x,y"
    return core.elwise_binary("!=", x,y)
    
def power(x, y):
    "Applies function power elementwise to arguments x,y"
    return core.elwise_binary("**", x,y)
    
def subtract(x, y):
    "Applies function subtract elementwise to arguments x,y"
    return core.elwise_binary("-", x,y)
    