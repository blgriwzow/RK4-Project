##This is a code for RK4     by Juan Pedro Saavedra  ##

import math
import numpy
import matplotlib



###########************#########
def dydx(y,x):
    fxy = x*(math.cos(x)) + x*y
    return fxy

    ##here is the function, modify if necesary also call F(x,y)##

#def yn(y): this is going to convert into the plot function 
    

    #yn = 
    #print(yn)
    #return yn


########*********########
##The h size should be able to ne choosen, also here is declaring the ##
##initial condition to solve (aproximate) the function of that solve the diff.eq ##

def main():
    ycero = 2/15
    xcero = 0
    x = xcero
    xcounter = xcero

    ##The initial condition user define its##

    yAprox = ycero

    h = 0.3

    while True:

        kOne= dydx(yAprox, x)

        x =  float (x + h/2)

        y = yAprox + kOne*h/2

        kTwo= dydx(y,x)

        y = yAprox + kTwo*h/2

        kThree = dydx(y,x)

        #Here is where stops using yn function#

        y = yAprox + kThree*h
        
        xcounter = xcounter + h


        ## This may be the breaking loop for K'sn##

        x = xcounter


        kFour = dydx(y,x)

        m = (1/6) * (kOne + 2 * kTwo + 2 * kThree + kFour )

        yAprox = yAprox +  (m * h)

        #### Here goes an arrey to save all the values ###

        ## Here is step number one, giving a first aproximation ##
        if x >= 1.5:
           break
        
    print('ITS DONE! , now lets plot this :D ')



    print(x,'space', kThree, 'Space', yAprox)
main()
## Calling the plot function 
