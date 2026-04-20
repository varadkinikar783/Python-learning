# The If statement is used to check whether a condition is true and execute a block of code if it is true.
# The else statement is used to execute a block of code if the condition is false. 
#these statements rely on boolean values
X = float(input("type a real no.: "))
if X >= 0:
    print("that's a positive real no.")
else: print("that's a negative real no.")
#now u can also use if as follows:
age = float(input("whats ur age? "))
if age < 0:
    print("the fuck is a sperm doing here??")
elif age in range(0, 20):
    print('you are still young!')
elif age in range(20, 32):
    print('wow! u are in the prime of your life!')
elif age in range(35, 100):
    print("getting old soldier!! ")        
# This allows u to have multiple printable statements for differnt contions that come from the same input  
Y = (input("type any no.:   "))
if type(Y) == float:
    print("that's a decimal no.")
elif type(Y) == int:
    print("that's an integer!")
else: print("enter an integer or a decimal no. only!")    