# HW2 Assignment
# Authors: <Michael Jameson>

# BE SURE TO IMPORT THE MODULES OR IDENTIFIERS THAT YOU
# NEED FOR EACH QUESTION

# ---------------------------------------------------------
# ---------------------------------------------------------
# Part 1
import math
from math import factorial, pi

def myCos(x):
    myCos = 1-(x**2)/factorial(2) +(x**4)/factorial(4) -(x**6)/factorial(6) +(x**8)/factorial(8) -(x**10)/factorial(10)
    print("Cos(", x,")=", myCos)
    return(myCos)
myCos(3.1416)
myCos(0)
myCos(6.2832)
myCos(pi/2)
myCos(3*pi/2)
myCos(-pi)

#   The taylor series for cosx= 3.1416 is -1.001829154863163
#   The taylor series for cosx= 0 is 1.0
#   The taylor series for cosx= 6.2832 is -5.438422238161426
#   The taylor series for cosx= 1.5707963267948966 is -4.6476600836607633e-07
#   The taylor series for cosx= 4.71238898038469 is -0.22244102459032433
#   The taylor series for cosx= -3.141592653589793 is -1.0018291040136216


# Part 2
def taylorCos(x,n):
    for i in range(1,n):
        return(i)
    taylorCos = ((-1)**i)((x**(2*i))/factorial(2*i))
    print ("The taylor series for cosx=", x,"is", taylorCos)
    return(taylorCos)
taylorCos(3.1416,6)
taylorCos(0,6)
taylorCos(6.2832,6)
taylorCos(pi/2,6)
taylorCos(3*pi/2,6)
taylorCos(-pi,6)

#   Copy debugging output into comment lines here.

#   Indicate here that you are claiming extra credit for
#   Part 2 ______________

#   Copy your extra credit version of taylorCos() here if
#   it is different from your original version.

# ---------------------------------------------------------
# Part 3
def arithmeticSequence(a0, d, n):
    "Delete this line and write the function body here."

#   Copy test output here

# ---------------------------------------------------------
# Part 4
def generateSamples(low, high, number):
    "Delete this line and write the function body here."

#   Copy test output here

# ---------------------------------------------------------
# Part 5
def plotRealCosVersusComputed(low, high, number, taylorN):
    "Delete this line and write the function body here."

#   Fill the estimated x value where the Taylor cos (with
#   six terms in the series) diverges from the actual cos
#   function:________

#   Submit your plot as a separate file

# End of homework.
