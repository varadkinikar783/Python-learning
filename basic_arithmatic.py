# for the four basic arithmetic operations, we can use the following functions:
# here we are considering a control variable 'X'
X = 10
# addition
X += 5  #here 5 will get added to X and the form '+=' is called augmented form of addition
print(X)
#substraction, multiplication, division, follow the same formate as addition; we just use * & / to multiply & divide respectively
#for exponentials we can use the '**' operator
#for e.g. X to the pawer 2,5,4 can be shown as:
X **= 2
print(X)
A = X**1
print(A)
#both ln 9 and 10 give the same result the first is augmented and second isn't
X **= 5
Z = X**4
print(Z)
#we can also use the modulus operator '%' to get the remainder of a division operation
# for e.g. let a variable be valued at 19 if we divide it by 4 the remainder will be 3, we can use the modulas function to demonstrate this as follows:
Y = 19
D = Y % 4
print(D)
# we can round a number to a it's closest int by using round function as follows:
K = 6.63
F = round(K)
print(F)
# the modulus function in maths is representated by the abs function:
I = -9
I = abs(I)
print(I)
# let's combine them
T = -9.78
T = round(abs(T))
print(T)
# to raise a no.(base) to a power(exponent) we can use the pow function as follows:
B = pow(2,3) # here 2 is the base and 3 is the exponent, this will give us 2 to the power of 3 which is 8
print(B)
# u can decide upto hoe many decimal points u want to round a number as follows:
C = 3.141592653589793
D = round(C, 2) # this will round C to 2 decimal places
print(D)
# i know ur memory is shit but remember the use of import math function