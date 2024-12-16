##This is a code for RK4     by Juan Pedro Saavedra  ##

import math
import numpy
import matplotlib.pyplot as plt



###########************#########
def dydx(y,x):
    fxy = x*(math.sin(x**2)) + x*y
    return fxy

    ##here is the function, modify if necesary also call F(x,y)##



########*********########
##The h size should be able to ne choosen, also here is declaring the ##
##initial condition to solve (aproximate) the function of that solve the diff.eq ##

def main():
    ycero = -7/15
    xcero = 0
    x = xcero
    xcounter = xcero

    ##The initial condition user define its##

    yAprox = ycero

    h = float(input('please tell me the step size h '))

    xpoint = [x]
    ypoint = [yAprox]

    

    while True:

        kOne= dydx(yAprox, x)

        x =  float (x + h/2)

        y = yAprox + kOne*h/2

        kTwo= dydx(y,x)

        y = yAprox + kTwo*h/2

        kThree = dydx(y,x)

        #Here is where stops using half steps for k's #

        y = yAprox + kThree*h
        
        xcounter = round( xcounter + h , 4)


        ## This may be the breaking loop for K'sn ##

        x = xcounter


        kFour = dydx(y,x)

        m = (1/6) * (kOne + 2 * kTwo + 2 * kThree + kFour )

        yAprox = yAprox +  m * h


        ## Calculating k4, m and the new yAprox = y(subn) ##

        xpoint.append(x)
        ypoint.append(yAprox)
        
        if x >= 1.5:
           break
        
    print('ITS DONE! , now lets plot this :D ')


    print(x, yAprox)

    plt.scatter(xpoint,ypoint)
    plt.show()
    
main()
## Calling main ## end of program ##

