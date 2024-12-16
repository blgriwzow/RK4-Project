##This is a code for RK4     by Juan Pedro Saavedra  ##

import math
import numpy as np
import matplotlib.pyplot as plt



###########************#########
def dydx(y,x):
    fxy = x*(math.cos(x)) + x*y
    return fxy

    ##here is the function, modify if necesary also call F(x,y)##


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

    xpoint = [x]
    ypoint = [yAprox]

    h = float(input('Enter the h value step, careful with the size ! '))

    while True:

        kOne= dydx(yAprox, x)

        x =  float (x + h/2)

        y = yAprox + kOne*h/2

        kTwo= dydx(y,x)

        y = yAprox + kTwo*h/2

        kThree = dydx(y,x)

        #Here is where stops using yn function#

        y = yAprox + kThree*h
        
        xcounter = round(xcounter + h , 4)


        ## This may be the breaking loop for K'sn##

        x = xcounter


        kFour = dydx(y,x)

        m = (1/6) * (kOne + 2 * kTwo + 2 * kThree + kFour )

        yAprox = yAprox +  (m * h)

        #### Here goes an arrey to save all the values ###

        xpoint.append(x)
        ypoint.append(yAprox)

        ## Here is step number one, giving a first aproximation ##
        if x >= 1.5:
           break
        
    print('ITS DONE! , now lets plot this :D ')

    print(x, yAprox)


    plt.scatter(xpoint,ypoint)
    plt.show()
main()
## Calling the plot function 
