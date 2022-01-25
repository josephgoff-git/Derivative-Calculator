import math
from math import sin, cos, tan
from math import pi
from math import e
from math import log
from math import *

A = input('Enter Function f(x): ')
B = int(input('Enter Smallest x in Interval: '))
C = int(input('Enter Largest x in Interval: '))
xs = float(input("Enter a first guess for a 0: "))

h = .0001

D1 = []          #list of first derivatives
D2 = []          #list of second derivatives
XX = []          #x values
YY = []          #Y values

for a in range(B, C):
    for b in range(10):
        XX.append(float(a) + (float(b) / 10))
for x in list(XX):
    YY.append(eval(A))
for x1 in list(XX):
    x = x1
    m = eval(A)
    x = x1-h
    f = eval(A)
    x = x1+h
    g = eval(A)
    val = ((g-f)/(2*h))
    D1.append(val)
    lav = ((g-2*m+f)/(h**2))
    D2.append(lav)

print("For each 0.1 increase in x: ")
print("f'(x) = ")
print(D1)
print("f''(x) = ")
print(D2)
print( )
print("Taking your guess, we will estimate the zero using Newton's Method: ")
print(xs)
xf=10000000
n=0
while (xf-xs) > h or (xf-xs) < -h and n < 100:
    xf=xs
    x=xs
    y=(eval(A))
    x=xs+h
    yup=(eval(A))
    x=xs-h
    yd=(eval(A))
    deriv=(yup-yd)/(2*h)
    xs=xs-(y/deriv)
    print(round(xs,8))
    n=n+1
if n>99:
    print("sorry, we can't find a 0")
   
