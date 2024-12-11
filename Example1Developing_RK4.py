##This is a code for RK4     by Juan Pedro Saavedra  ##

import math

ycero = 0.5

##The initial condition user define its##

y = ycero

h=0.5

###########************#########
def dydx():
    fxy = 2*y
    return fxy

    ##here is the function, modify if necesary also call F(x,y)##

#def yn():
   # yn = y + kOne * h/2
    #return yn
########*********########
##The h size should be able to ne choosen, also here is declaring the ##
##initial condition to solve (aproximate) the function of that solve the diff.eq ##


kOne= dydx()

y = ycero + kOne * h/2 

kTwo= dydx()

y = ycero + kTwo * h/2

kThree = dydx()

y = ycero + kThree * h


## This may be the breaking loop for K'sn##

kFour = dydx()

m = (1/6) * (kOne + 2 * kTwo + 2 * kThree + kFour )

yAprox = ycero + m * h

## Here is step number one, giving a first aproximation ##



#*Here is where the step two is staring  *#

yOne = yAprox

## ##


print(kThree, yAprox )
