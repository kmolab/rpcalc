#!/usr/bin/env python3
# rpcalc operators using stack datatype
# for more info, see github.com/qguv/rpcalc

# If an error is thrown in a binary operation,
# the erroneous operator is discarded and the
# proper operator is kept.

# If an error is thrown in a unary operation,
# the operator is discarded.

import math
from random import random

# Add your own here! Make sure to add a binding too.


#### Stack ####

def Drop(stack):
    null = stack.pop()

def Clear(stack):
    stack.items = list()

def Length(stack):
    return stack.name + " has " + str(len(stack)) + " entries."

def DupX(stack): # currently not used;
                 # functionality given by
                 # `Enter` with empty buf
    a = stack.pop()
    stack.push(a)
    stack.push(a)

def SwapXY(stack):
    x = stack.pop()
    y = stack.pop()
    stack.push(x)
    stack.push(y)


#### Arithmetic ####

def Add(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a + b)

def Subtract(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a - b)

def Multiply(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a * b)

def Divide(stack):
    b = stack.pop()
    a = stack.pop()
    if b == 0:
        stack.push(a) # return dividend to stack
        # divisor (0) gets the boot
        return "can't divide by 0!"
    else:
        r = a / b
        stack.push(r)

def Negate(stack):
    a = stack.pop()
    stack.push(-1 * a)

def Modulus(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a % b)

def Floor(stack):
    a = stack.pop()
    stack.push(math.floor(a))

def Ln(stack):
    a = stack.pop()
    if a <= 0: 
        return "out of domain!"
    else:
        r = math.log(a)
        stack.push(r) # push the answer

def Power(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a ** b)

def SqRoot(stack):
    a = stack.pop()
    if (a < 0):
        return "imaginary numbers not supported!"
    else:
        r = math.sqrt(a)
        stack.push(r)

def Absolute(stack):
    a = stack.pop()
    r = abs(a)
    stack.push(r)

def Factorial(stack):
    a = stack.pop()
    if (a < 0):
        return "out of domain!"
    elif (int(a) != a):
        return "not integral!"
    else:
        r = math.factorial(int(a))
        stack.push(r)


#### Sequence Operators ####

def MakeList(stack):
# another utility function,
# this time for sequences
    r = [ stack.pop() for null in range(len(stack)) ]
    return r

def Summation(stack):
    r = math.fsum(MakeList(stack))
    stack.push(r)

def Product(stack):
    seq = MakeList(stack)
    r = 1
    for element in seq:
        r = r * element
    stack.push(r)


#### Statistics ####

def Mean(stack):
    seq = MakeList(stack)
    r = sum(seq) / len(seq)
    stack.push(r)

def Median(stack):
    ord = sorted(MakeList(stack))
    if len(ord) % 2 == 1:
    # if only one middle number, return that
        choose = math.floor(len(ord) / 2)
        r = ord[choose]
    else:
    # if two middle numbers, return average
        iE = int(len(ord) / 2 + 1)
        iS = iE - 2
        r = sum(ord[iS:iE]) / 2
    stack.push(r)


#### Constants ####

def ConstPi(stack):
    r = math.pi
    stack.push(r)

def ConstE(stack):
    r = math.e
    stack.push(r)


#### Logic ####

def EqTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a == b else 0
    stack.push(r)

def NotTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a != b else 0
    stack.push(r)

def LtTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a < b else 0
    stack.push(r)

def GtTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a > b else 0
    stack.push(r)

def LtEqTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a <= b else 0
    stack.push(r)

def GtEqTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a >= b else 0
    stack.push(r)


#### Trigonometry ####

def TrigRoundFix(roughAnswer):
# Not an operator, but a utility
# function that fixes rounding
# errors in Trig functions which
# prevent the expected answers:
# 1, 0, and -1.
    r = roughAnswer
    if abs(r) < 1e-15:
        r = 0.0
    elif abs(r-1) < 1e-15:
        r = 1.0
    elif abs(r+1) < 1e-15:
        r = -1.0
    return r

def Sine(stack):
    a = stack.pop()
    r = math.sin(a)
    r = TrigRoundFix(r)
    stack.push(r)

def Cosine(stack):
    a = stack.pop()
    r = math.cos(a)
    r = TrigRoundFix(r)
    stack.push(r)

def Tangent(stack):
    a = stack.pop()
    r = math.tan(a)
    r = TrigRoundFix(r)
    stack.push(r)

def Arcsine(stack):
    a = stack.pop()
    if (a > 1) or (a < -1):
        return "out of domain!"
    else:
        r = math.asin(a)
        r = TrigRoundFix(r)
        stack.push(r)

def Arccosine(stack):
    a = stack.pop()
    if (a > 1) or (a < -1):
        return "out of domain!"
    else:
        r = math.acos(a)
        r = TrigRoundFix(r)
        stack.push(r)

def Arctangent(stack):
    a = stack.pop()
    r = math.atan(a)
    r = TrigRoundFix(r)
    stack.push(r)

def ToDegrees(stack):
    a = stack.pop()
    r = math.degrees(a)
    stack.push(r)

def ToRadians(stack):
    a = stack.pop()
    r = math.radians(a)
    stack.push(r)


#### Others ####

def Random(stack):
    stack.push(random())

def DebugIter(stack):
    a = stack.pop()
    a_ = int(math.floor(a)) # a-prime
    for i in range(1, (a_ + 1)):
        stack.push(i)
    return "pushed " + str(a_) + " entries."

# Bindings cannot include any of the following
# characters for technical reasons: Q p
# Bindings must not begin with the name of
# another binding. For instance, =< was chosen
# over <= because it does not begin with (and
# therefore does not conflict with) <.
bindings = {
    # Key is the arithmetic keypress
    # Value[0] is the paired function
    # Value[1] is the argument requirement
        #### Stack
        'D' :   [Drop      , 1],
        'C' :   [Clear     , 1],
        '#' :   [Length    , 0],
        'w' :   [SwapXY    , 2],
        #### Arithmetic
        '+' :   [Add       , 2],
        '-' :   [Subtract  , 2],
        '*' :   [Multiply  , 2],
        'x' :   [Multiply  , 2],
        '/' :   [Divide    , 2],
        'n' :   [Negate    , 1],
        '%' :   [Modulus   , 2],
        'f' :   [Floor     , 1],
        'ln':   [Ln        , 1],
        '^' :   [Power     , 2],
        'sqrt': [SqRoot    , 1],
        'abs' : [Absolute  , 1],
        '!' :   [Factorial , 1],
        #### Sequence Operators
        'S' :   [Summation , 1],
        'P' :   [Product   , 1],
        #### Statistics
        'mean': [Mean      , 1],
        'med' : [Median    , 1],
        #### Constants
        'ke':   [ConstE    , 0],
        'kpi' : [ConstPi   , 0],
        #### Logic
        '==':   [EqTest    , 2],
        '=!':   [NotTest   , 2],
        '<' :   [LtTest    , 2],
        '>' :   [GtTest    , 2],
        '=<':   [LtEqTest  , 2],
        '=>':   [GtEqTest  , 2],
        #### Trigonometry
        'sin' : [Sine      , 1],
        'cos' : [Cosine    , 1],
        'tan' : [Tangent   , 1],
        'asin': [Arcsine   , 1],
        'acos': [Arccosine , 1],
        'atan': [Arctangent, 1],
        'deg' : [ToDegrees , 1],
        'rad' : [ToRadians , 1],
        #### Others
        'rand': [Random    , 0],
        'debug':[DebugIter , 1], #DEBUG
        }
