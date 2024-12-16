##This is a code for RK4     by Juan Pedro Saavedra  ##

import math
import matplotlib.pyplot as plt
import numpy as np



###########************#########
def dydx(y):
    fxy = 2*y
    return fxy

    ##here is the function, modify if necesary also call F(x,y)##

def yn(y,k,h):
    
    yn = y + k * h/2
    return yn

########*********########
##The h size should be able to ne choosen, also here is declaring the ##
##initial condition to solve (aproximate) the function of that solve the diff.eq ##
    

def main():
    ycero = 0.5
    xcero = 0
    x = xcero

    ##The initial condition user define its##

    yAprox = ycero

    print('Please introduce the step size you want to take, careful with your step size !!' )
          #The smaller the step, accurcy will increase')

    h = float(input())

    # h = 0.5 ## Make the step size constant
    
    xpoint = [x]
    ypoint = [yAprox]

    while True :

        kOne= dydx(yAprox)

        y = yn(yAprox,kOne,h)

        kTwo= dydx(y)

        y = yn(yAprox,kTwo,h)

        kThree = dydx(y)

    #Here is where stops using yn function#

        y = yAprox + kThree * h
    
        x = round(x + h, 4) 


    ## This may be the breaking loop for K'sn##

        kFour = dydx(y)

        m = (1/6) * (kOne + 2 * kTwo + 2 * kThree + kFour )

        yAprox = yAprox + m * h
        ## Calculating k4, m, and the new yAprox = y(subn) ##

        xpoint.append(x)
        ypoint.append(yAprox)


        if x >= 1:
            break

    ## Adding the last poin to fix the graph ##


    print(x,'Space', yAprox)
    plt.scatter(xpoint,ypoint)
    plt.show()



    #*Here is where the step two is staring  *#


    ## ##


    print(x,'Space', yAprox)
main()
