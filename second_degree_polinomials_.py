## This is just a program to get the roots of a polinomial of second degree

import math

print('Hi user, this  program will use the coeficent \
      of a 2nd degree polynomial and solve it (only for real roots)  ')

print('Here is for ax^2 ')

a= float(input())

print('Here is for bx ')

b= float (input())

print('Here is for c')

c= float(input())

##Asking for the coeficients 

dis= (b**2) - 4*a*c

if dis < 0:
    print('your response is in the complex world ')
    
##This is the discrimenant calculetor
else:

    disroot= math.sqrt(dis)

    ## Calculating the 

    pos_x= (-b+disroot)/(2*a)
    neg_x= (-b-disroot)/(2*a)

    ##Calculationg the roots + and - 

    print('Here is the positive root '+ str(pos_x))
    print('Here is the negative root ' + str(neg_x))


    ## Here ends hopes it works 
